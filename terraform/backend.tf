terraform {
  backend "gcs" {
    bucket = "stonkspy-bucket"
    prefix = "terraform/state"
  }
}