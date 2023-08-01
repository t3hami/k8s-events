# Kubernetes Event Based Workloads


Workload defination
    Create
    Store in Database
Create the defined workload
    Status (All, running, completed, failed)
    Trigger history/source
    Store in Database
Advance
    Authentication
    Logs
UI
    Workload definations
    Status
    Trigger history/source
    Logs ?
    auth


TOKEN=$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)

curl -k -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  --data-binary @helloworld-job.json \
  https://$KUBERNETES_SERVICE_HOST/apis/batch/v1/namespaces/default/jobs
