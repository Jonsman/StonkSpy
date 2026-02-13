# Google Cloud services needed
variable "gcp_service_list" {
  description = "List of APIs to enable"
  type        = list(string)
  default = [
    "run.googleapis.com",                   # For Cloud Run
    "artifactregistry.googleapis.com",      # For Docker Images
    "iam.googleapis.com",                   # For Service Accounts
    "cloudresourcemanager.googleapis.com",  # For managing project resources
    "aiplatform.googleapis.com"             # For Vertex AI access
  ]
}

# Enable the services
resource "google_project_service" "enabled_services" {
  for_each = toset(var.gcp_service_list)
  project  = var.project_id
  service  = each.key

  # IMPORTANT: Prevent Terraform from disabling the API if you delete the resource
  # This avoids accidental downtime for other things in your project.
  disable_on_destroy = true
}

# Artifact Registry
resource "google_artifact_registry_repository" "repo" {
  location      = var.region
  repository_id = "${var.app_name}-repo"
  description   = "docker repository"
  format        = "DOCKER"
}

# Service Accounts
resource "google_service_account" "agent_sa" {
  account_id   = "${var.app_name}-agent-sa"
  display_name = "Service Account for Agent with Vertex AI access"
}

resource "google_service_account" "frontend_sa" {
  account_id   = "${var.app_name}-frontend-sa"
  display_name = "Service Account for Frontend"
}

# Allow Agent Vertex AI access
resource "google_project_iam_member" "vertex_ai_user_agent" {
  project = var.project_id
  role    = "roles/aiplatform.user" # Allows using Vertex AI resources
  member  = "serviceAccount:${google_service_account.agent_sa.email}"
}

# Frontend
resource "google_cloud_run_v2_service" "frontend" {
  name     = "frontend-cloudrun-service"
  location = var.region
  deletion_protection = false
  ingress = "INGRESS_TRAFFIC_ALL"

  template {
    service_account = google_service_account.frontend_sa.email
    health_check_disabled = true
    containers {
      image = "${var.region}-docker.pkg.dev/${var.project_id}/${google_artifact_registry_repository.repo.repository_id}/frontend:latest"
      resources {
        limits = {
          cpu    = "2"
          memory = "1024Mi"
        }
      }
    }
  }
}

# Make Frontend public
resource "google_cloud_run_v2_service_iam_binding" "frontend" {
  project  = var.project_id
  location = google_cloud_run_v2_service.frontend.location
  name     = google_cloud_run_v2_service.frontend.name
  role     = "roles/run.invoker"
  members  = [
    "allUsers"
  ]
}

# Agent Backend
resource "google_cloud_run_v2_service" "agent" {
  name     = "agent-cloudrun-service"
  location = var.region
  deletion_protection = false
  ingress = "INGRESS_TRAFFIC_ALL"

  template {
    service_account = google_service_account.agent_sa.email
    health_check_disabled = true
    containers {
      image = "${var.region}-docker.pkg.dev/${var.project_id}/${google_artifact_registry_repository.repo.repository_id}/agent:latest"
      resources {
        limits = {
          cpu    = "2"
          memory = "1024Mi"
        }
      }
      env {
        name  = "PROJECT_ID"
        value = var.project_id
      }
      env {
        name  = "GCP_REGION"
        value = var.region
      }
      env {
        name  = "VERTEXAI_MODEL"
        value = var.vertexai_model
      }
      env {
        name  = "GOOGLE_GENAI_USE_VERTEXAI"
        value = "TRUE"
      }
    }
  }
}

# Make Agent Backend public
resource "google_cloud_run_v2_service_iam_binding" "agent" {
  project  = var.project_id
  location = google_cloud_run_v2_service.agent.location
  name     = google_cloud_run_v2_service.agent.name
  role     = "roles/run.invoker"
  members  = [
    "allUsers"
  ]
}

