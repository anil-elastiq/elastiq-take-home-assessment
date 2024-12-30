# OpenSearch Deployment Using Kubernetes Operator

## Objective
Deploy an OpenSearch solution using the OpenSearch Operator on a Kubernetes cluster hosted in **GCP Autopilot**, **GKE Standard**, or an equivalent platform on **AWS** or **Azure**.

## Prerequisites
1. **Kubernetes Cluster**: A Kubernetes cluster must already exist. This guide assumes GKE, but it can be adapted for AWS EKS or Azure AKS.
2. **CLI Tools**:
   - `kubectl`
   - `terraform`
   - Cloud provider CLI (`gcloud`, `aws-cli`, or `azure-cli`)
3. **Permissions**:
   - Sufficient permissions to manage Kubernetes resources.
   - GCP Workload Identity enabled (if deploying to GKE).

---

## Steps

### Step 1: Configure Kubernetes Cluster Access

1. **Authenticate to the cluster**:
   - For GKE:
     ```bash
     gcloud container clusters get-credentials <CLUSTER_NAME> --region <REGION>
     ```
   - For AWS:
     ```bash
     aws eks update-kubeconfig --name <CLUSTER_NAME> --region <REGION>
     ```
   - For Azure:
     ```bash
     az aks get-credentials --name <CLUSTER_NAME> --resource-group <RESOURCE_GROUP>
     ```

2. Verify cluster access:
   ```bash
   kubectl get nodes
   ```

---

### Step 2: Install OpenSearch Operator

1. Clone the OpenSearch Operator repository:
   ```bash
   git clone https://github.com/opensearch-project/opensearch-k8s-operator.git
   cd opensearch-k8s-operator
   ```

2. Apply the Operator manifests:
   ```bash
   kubectl apply -f config/samples/opensearch-cluster.yaml
   kubectl apply -f config/samples/opensearch-dashboard.yaml
   ```

3. Verify Operator deployment:
   ```bash
   kubectl get pods -n opensearch-operator-system
   ```

---

### Step 3: Deploy OpenSearch Cluster

1. Create a namespace for OpenSearch:
   ```bash
   kubectl create namespace opensearch
   ```

2. Deploy OpenSearch resources:
   - Create a `CustomResource` for the OpenSearch cluster:
     ```yaml
     apiVersion: opensearch.opster.io/v1
     kind: OpenSearchCluster
     metadata:
       name: opensearch-cluster
       namespace: opensearch
     spec:
       general:
         version: "2.8.0"
       nodePools:
         - name: master
           replicas: 3
           roles:
             - master
         - name: data
           replicas: 2
           roles:
             - data
     ```
   - Apply the configuration:
     ```bash
     kubectl apply -f opensearch-cluster.yaml
     ```

3. Verify deployment:
   ```bash
   kubectl get pods -n opensearch
   ```

---

### Step 4: Configure Secure Access (GCP Workload Identity)

1. Create a Google Service Account (GSA):
   ```bash
   gcloud iam service-accounts create opensearch-sa --description="OpenSearch service account" --display-name="OpenSearchSA"
   ```

2. Bind the GSA to the Kubernetes Service Account (KSA):
   ```bash
   gcloud iam service-accounts add-iam-policy-binding opensearch-sa@<PROJECT_ID>.iam.gserviceaccount.com \
     --role roles/iam.workloadIdentityUser \
     --member "serviceAccount:<PROJECT_ID>.svc.id.goog[opensearch/default]"
   ```

3. Annotate the Kubernetes Service Account:
   ```bash
   kubectl annotate serviceaccount default \
     --namespace opensearch \
     iam.gke.io/gcp-service-account=opensearch-sa@<PROJECT_ID>.iam.gserviceaccount.com
   ```

---

### Step 5: Validate OpenSearch Deployment

1. Check OpenSearch health:
   ```bash
   kubectl exec -n opensearch <POD_NAME> -- curl -X GET http://localhost:9200/_cluster/health?pretty
   ```

2. Access the OpenSearch Dashboard:
   - Port-forward the dashboard service:
     ```bash
     kubectl port-forward -n opensearch svc/opensearch-dashboard 5601:5601
     ```
   - Open your browser and navigate to `http://localhost:5601`.

---

### Step 6: Apply Cost Optimization

1. **Enable Auto-scaling**:
   - Use Horizontal Pod Autoscalers (HPA):
     ```bash
     kubectl autoscale deployment opensearch --cpu-percent=80 --min=2 --max=5
     ```

2. **Use Preemptible/Spot Instances**:
   - Configure node pools for cost optimization.

3. **Resource Requests and Limits**:
   - Add resource configurations to pods:
     ```yaml
     resources:
       requests:
         cpu: 500m
         memory: 1Gi
       limits:
         cpu: 1000m
         memory: 2Gi
     ```

---

## Deliverables

1. **Credentials**:
   - Provide GCP/AWS/Azure credentials or kubeconfig for cluster validation.

2. **Terraform Code**:
   - Infrastructure setup using Terraform (e.g., cluster creation, Workload Identity).

3. **Documentation**:
   - This README, including instructions for deployment, validation, and best practices.

---

## Best Practices

1. Follow the principle of least privilege for RBAC and IAM roles.
2. Apply network policies to restrict pod-to-pod communication.
3. Enable Kubernetes node auto-upgrade and auto-repair.
4. Monitor logs and metrics using Prometheus/Grafana or cloud-native tools.
5. Regularly review and optimize costs.

