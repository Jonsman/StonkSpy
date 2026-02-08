variable "project_id" {
  description = "Google Cloud Project ID"
  type        = string
}

variable "region" {
  description = "GCP Region for the Resources"
  type        = string
  default     = "europe-north1"
}

variable "app_name" {
  type    = string
  default = "stonkspy"
}

variable "vertexai_model" {
  description = "Vertex AI Model Name"
  type        = string
  default     = "gemini-2.5-pro"
}