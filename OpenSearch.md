# OpenSearch Deployment with Operator on GKE Autopilot using Terraform

# Main Terraform Configuration for GKE Autopilot Cluster and OpenSearch Installation

provider "google" {
  project = var.project_id
  region  = var.region
}

# Create a GKE Autopilot Cluster
resource "google_container_cluster" "gke_autopilot" {
  name     = "opensearch-cluster"
  location = var.region

  enable_autopilot = true

  workload_identity_config {
    identity_namespace = "${var.project_id}.svc.id.goog"
  }
}

# Create a Kubernetes Namespace for OpenSearch
resource "kubernetes_namespace" "opensearch" {
  metadata {
    name = "opensearch"
  }
}

# Grant Workload Identity Permissions for OpenSearch Operator
resource "google_service_account" "opensearch_operator" {
  account_id   = "opensearch-operator"
  display_name = "OpenSearch Operator Service Account"
}

resource "google_project_iam_binding" "opensearch_operator_bind" {
  project = var.project_id
  role    = "roles/iam.workloadIdentityUser"

  members = [
    "serviceAccount:${var.project_id}.svc.id.goog[opensearch/opensearch-operator]"
  ]
}

# Deploy OpenSearch Operator YAML
resource "kubernetes_manifest" "opensearch_operator" {
  manifest = {
    "apiVersion" = "apps/v1"
    "kind"       = "Deployment"
    "metadata" = {
      "name"      = "opensearch-operator"
      "namespace" = "opensearch"
    }
    "spec" = {
      "replicas" = 1
      "selector" = {
        "matchLabels" = {
          "app" = "opensearch-operator"
        }
      }
      "template" = {
        "metadata" = {
          "labels" = {
            "app" = "opensearch-operator"
          }
        }
        "spec" = {
          "serviceAccountName" = "opensearch-operator"
          "containers" = [
            {
              "name"  = "opensearch-operator"
              "image" = "opensearchproject/opensearch-operator:latest"
            }
          ]
        }
      }
    }
  }
}

# Create OpenSearch Cluster Custom Resource
resource "kubernetes_manifest" "opensearch_cluster" {
  manifest = {
    "apiVersion" = "opensearch.opensearch.org/v1"
    "kind"       = "OpenSearchCluster"
    "metadata" = {
      "name"      = "opensearch-cluster"
      "namespace" = "opensearch"
    }
    "spec" = {
      "general" = {
        "version" = "2.9.0"
      }
      "nodePools" = [
        {
          "name"     = "master"
          "replicas" = 3
          "roles"    = ["master"]
          "resources" = {
            "requests" = {
              "cpu"    = "500m"
              "memory" = "1Gi"
            }
          }
        },
        {
          "name"     = "data"
          "replicas" = 3
          "roles"    = ["data"]
          "resources" = {
            "requests" = {
              "cpu"    = "1"
              "memory" = "2Gi"
            }
          }
        }
      ]
    }
  }
}

# Outputs
output "cluster_name" {
  value = google_container_cluster.gke_autopilot.name
}

output "cluster_location" {
  value = google_container_cluster.gke_autopilot.location
}

output "opensearch_endpoint" {
  value = "http://opensearch-cluster-opensearch.${var.region}.svc.cluster.local:9200"
}
