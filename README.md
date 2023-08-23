## Docker image builder

### Getting started
To build a new image:

**CI/CD > Run pipeline**

Enter two mandatory variables:

* **BUILD** - This is repo name on Docker Hub same as subdirectory under dockerfiles (e.g. *debug_tools*).
* **TAG** - New tag for image (e.g. *0.16*).

### Kubernetes example
```bash
kubectl run debug-pod --rm -i -n <ns> --tty --image glowcow/debug_tools:0.16 -- /bin/bash
```

```bash
curl -H "Authorization: Bearer $(cat $TOKEN_PATH)" --cacert $CA_CERT_PATH -X POST -H "Content-Type: application/json" --data '{
  "apiVersion": "batch/v1",
  "kind": "Job",
  "metadata": {
    "name": "example-job"
  },
  "spec": {
    "template": {
      "spec": {
        "restartPolicy": "OnFailure",
        "containers": [
          {
            "name": "example-job-container",
            "image": "busybox ",
            "command": ["echo", "Hello, World!"]
          }
        ]
      }
    }
  }
}' https://kubernetes.default/apis/batch/v1/namespaces/jobs-prod/jobs
```