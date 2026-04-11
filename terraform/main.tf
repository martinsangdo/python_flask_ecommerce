provider "kubernetes" {
  config_path = "~/.kube/config"
}

resource "kubernetes_namespace" "fastapi" {
  metadata {
    name = "fastapi"
  }
}