output "repository_url" {
  value       = google_artifact_registry_repository.repo.name
  description = "Artifact Registry Repository URL"
}

output "frontend_url" {
  value       = google_cloud_run_v2_service.frontend.uri
  description = "Frontend URL"
}

output "agent_backend_url" {
  value       = google_cloud_run_v2_service.agent.uri
  description = "Agent Backend URL"
}