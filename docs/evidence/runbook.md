# Apex Operations API — Operations Runbook

## 1. Purpose

This runbook describes how to deploy, verify, monitor, troubleshoot, and roll back the Apex Operations API.

The commands are intended for the Linux host where Docker Engine and Docker Compose are installed.

## 2. Prerequisites

- Linux host with Docker Engine installed.
- Docker Compose plugin installed.
- Project repository cloned.
- Required versioned Docker images available locally.

## 3. Start the Application

Navigate to the project directory:

```bash
cd /root/apex-operations-api
```

Select the application version:

```bash
export APP_VERSION=1.0.0
```

Start the application:

```bash
docker compose up -d --no-build
```

Check the container:

```bash
docker compose ps
```

## 4. Verify Application Health

Check the health endpoint:

```bash
curl http://localhost:8080/health
```

Expected response:

```json
{
  "status": "healthy"
}
```

Check the root endpoint:

```bash
curl http://localhost:8080/
```

Check readiness:

```bash
curl http://localhost:8080/ready
```

Check diagnostic information:

```bash
curl http://localhost:8080/metrics
```

## 5. View Application Logs

Display recent container logs:

```bash
docker compose logs --tail=100 api
```

Follow logs continuously:

```bash
docker compose logs -f api
```

Use logs to investigate HTTP requests and application errors.

## 6. Troubleshooting

### Container is not running

Check container status:

```bash
docker compose ps -a
```

Inspect logs:

```bash
docker compose logs api
```

### Health endpoint is unavailable

Check the container:

```bash
docker compose ps
```

Inspect application logs:

```bash
docker compose logs --tail=100 api
```

Confirm that the application is listening on port 8000 inside the container.

### Readiness returns HTTP 503

The readiness endpoint uses the `DEPENDENCY_AVAILABLE` environment variable.

To simulate an available dependency, set:

```bash
export DEPENDENCY_AVAILABLE=true
```

Recreate the container:

```bash
docker compose up -d --no-build --force-recreate
```

This is a simulation, not a real external dependency recovery procedure.

## 7. Release Deployment

Build a new version:

```bash
docker build --build-arg APP_VERSION=1.0.1 -t apex-operations-api:1.0.1 .
```

Deploy the new version:

```bash
export APP_VERSION=1.0.1
docker compose up -d --no-build --force-recreate
```

Verify the deployed version:

```bash
curl http://localhost:8080/
```

## 8. Rollback Procedure

If the new release has an issue, select the previously built image version:

```bash
export APP_VERSION=1.0.0
```

Recreate the application using the previous image:

```bash
docker compose up -d --no-build --force-recreate
```

Verify the rollback:

```bash
curl http://localhost:8080/
curl http://localhost:8080/health
```

Expected result: application version `1.0.0` and a healthy status.

The previous image must remain available locally.

## 9. Stop the Application

Stop and remove the Compose-managed container:

```bash
docker compose down
```

This does not remove the locally stored Docker images.

## 10. Operational Notes

- The Compose configuration binds the application to localhost.
- Application versions are selected through `APP_VERSION`.
- The Docker health check monitors the `/health` endpoint.
- Readiness currently uses a simulated dependency setting.
- The `/metrics` endpoint returns JSON diagnostics, not Prometheus metrics.
- Review container logs when investigating failures.

## 11. Recovery Scope

This runbook covers local container deployment and rollback on the assessment environment. It does not define production incident response, database recovery, or multi-host disaster recovery procedures.
