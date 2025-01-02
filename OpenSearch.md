# OpenSearch hosting in Kubernetes using Operator

## Objective
Host an open-source OpenSearch solution inside **Google Cloud Autopilot**, **GKE Standard**, or the equivalent on **AWS** or **Azure** using [Operator](https://github.com/opensearch-project/opensearch-k8s-operator)

> [!NOTE]
> **Deliverables:**
> 1. Provide necessary **credentials** (cloud account, API keys, etc.) to validate the solution.
> 1. **Terraform code**.
> 1. A brief documentation or **README** explaining the approach, best practices followed, and how to validate the deployment.

> [!TIP]
> Implement GCP Workload Identity for secure identity management and avoid static credentials.

> [!IMPORTANT]
> Please install OpenSearch only using the operator no helm or any other way to install it.

> [!CAUTION]
> - **K8S Best Practices:** Follow cloud security best practices for cluster setup and management e.g., least privilege principle, network policies, node auto-upgrade.
> - **Cost Optimized:** Ensure that all resources created follow cloud cost-optimization guidelines.
>
> # Selenium Playground Search Validation Test

This repository contains a Selenium-based test to validate the search functionality on the **Selenium Playground Table Search Demo**.

## Requirements
- Python 3.x
- Selenium
- pytest
- webdriver-manager

## Setup
1. Install Python dependencies using pip:
   ```bash
   pip install selenium pytest webdriver-manager


**Good luck!**
