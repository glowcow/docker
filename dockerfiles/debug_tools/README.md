## Examples

### 1. Using Kubernetes Service Account to create Jobs(for example):

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


### 2. Using the MinIO Client to work with S3 object store:

```bash
minc alias set <alias_name> https://s3.pi.glowcow.xyz <access_key> <access_secret>
```

Create bucket:

```bash
minc mb <ALIAS_NAME>/<BUCKET_NAME>
```

Upload file:

```bash
minc cp <LOCAL_PATH_TO_FILE> <ALIAS_NAME>/<BUCKET_NAME>/<DEST_PATH>
```

Upload directory:

```bash
minc cp --recursive <LOCAL_PATH_TO_DIRECTORY> <ALIAS_NAME>/<BUCKET_NAME>/<DEST_PATH>
```

Verify Upload:

```bash
minc ls <ALIAS_NAME>/<BUCKET_NAME>
```

Deleting a File:

```bash
minc rm <ALIAS_NAME>/<BUCKET_NAME>/<FILE_PATH>
```

Deleting a Directory:

```bash
minc rm --recursive <ALIAS_NAME>/<BUCKET_NAME>/<DIRECTORY_PATH>
```

### 3. Using the postgresql-client:

Connecting to a PostgreSQL database:

```bash
psql -h host -U username -d mydb
```

Running SQL command without entering interactive mode:

```bash
psql -h host -U username -d mydb -c "SELECT * FROM users;"
```

Backup a database:

```bash
pg_dump -h localhost -U username mydb > backup.sql
```
