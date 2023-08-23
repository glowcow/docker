## Docker image builder

### Getting started
To build a new image:

**CI/CD > Run pipeline**

Enter two mandatory variables:

* **BUILD** - This is repo name on Docker Hub same as subdirectory under dockerfiles (e.g. *debug_tools*).
* **TAG** - New tag for image (e.g. *0.17*).

### Kubernetes example
```bash
kubectl run debug-pod --rm -i -n <ns> --tty --image glowcow/debug_tools:0.17 -- /bin/bash
```