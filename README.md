# Apex Operations API

## 1. Project Overview

Apex Operations API is a sample DevOps assessment project demonstrating how to build, test, containerize, deploy, monitor, and roll back a Python API.

The project focuses on reproducible deployment, automated quality checks, application health, version management, and operational documentation.

This project uses synthetic application data and does not connect to Apex AI Arabia production systems or customer data.

## 2. Technology Stack

- **Language:** Python
- **API Framework:** FastAPI
- **Application Server:** Uvicorn
- **Containerization:** Docker
- **Container Orchestration:** Docker Compose
- **Testing:** Pytest
- **Code Quality:** Ruff
- **CI:** GitHub Actions
- **Version Control:** Git and GitHub
- **Environment:** AWS EC2 running Amazon Linux 2023

## 3. Project Structure

```text
.
├── .github/
│   └── workflows/
│       └── ci.yml
├── app/
│   └── main.py
├── docs/
│   └── evidence/
├── tests/
│   └── test_api.py
├── Dockerfile
├── compose.yaml
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

## 4. API Endpoints

| Endpoint | Method | Purpose |
|---|---|---|
| `/` | GET | Returns application name and version |
| `/health` | GET | Checks application health |
| `/ready` | GET | Checks application readiness |
| `/metrics` | GET | Returns version and dependency diagnostics |

### Example response

**GET /**

```json
{
  "application": "Apex Operations API",
  "version": "1.0.0"
}
```

**GET /health**

```json
{
  "status": "healthy"
}
```

**GET /ready**

```json
{
  "status": "ready"
}
```

Note: The readiness endpoint uses a configurable environment variable to simulate dependency availability. The metrics endpoint returns JSON diagnostics; it is not a Prometheus exporter.

## 5. Local Development

### Prerequisites

- Python 3.12
- Git
- Docker Engine
- Docker Compose

### Clone the repository

```bash
git clone https://github.com/hashimbasha072-byte/JUNIOR_DEVOPS_ENGINEER_PROJECT.git
cd JUNIOR_DEVOPS_ENGINEER_PROJECT
```

### Install dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
```

### Start the application

```bash
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Open `http://127.0.0.1:8000/docs` to view the interactive API documentation.

## 6. Automated Testing

Run the test suite:

```bash
pytest -v
```

Run code quality checks:

```bash
ruff check .
```

The test suite covers the API's main endpoints and readiness behavior.

## 7. Docker Build and Deployment

Build the application image:

```bash
docker build --build-arg APP_VERSION=1.0.0 -t apex-operations-api:1.0.0 .
```

Deploy using Docker Compose:

```bash
export APP_VERSION=1.0.0
docker compose up -d --no-build
```

Check the running container:

```bash
docker compose ps
```

Check the API:

```bash
curl http://localhost:8080/health
```

The Compose configuration binds the API to `127.0.0.1:8080` on the host.

## 8. Versioning and Rollback

Build a newer release:

```bash
docker build --build-arg APP_VERSION=1.0.1 -t apex-operations-api:1.0.1 .
```

Deploy version 1.0.1:

```bash
export APP_VERSION=1.0.1
docker compose up -d --no-build --force-recreate
```

Rollback to version 1.0.0:

```bash
export APP_VERSION=1.0.0
docker compose up -d --no-build --force-recreate
```

The previous image must remain available locally for this rollback procedure.

## 9. Continuous Integration

The GitHub Actions workflow is located at:

`.github/workflows/ci.yml`

It runs on pushes to the main branch, pull requests targeting main, and manual workflow dispatch.

The workflow performs:

1. Python environment setup.
2. Dependency installation.
3. Ruff code quality checks.
4. Pytest automated tests.
5. Docker image build verification.

## 10. Health Checks and Logging

The Docker image includes a health check that calls the application's `/health` endpoint.

The API logs HTTP request information, including the method, path, and response status code.

The `/ready` endpoint provides a basic readiness check using a configurable dependency-availability setting.

## 11. Security Considerations

- The application runs as a non-root user inside the container.
- The Docker image uses a slim Python base image.
- The application is bound to localhost in the Compose configuration.
- No production credentials or customer data are included.
- Application dependencies are pinned to specific versions.

## 12. Evidence

Implementation evidence is maintained in `docs/evidence/`, including:

- Successful automated test execution.
- Ruff code quality results.
- Intentional test failure demonstration.
- Versioned deployment and rollback results.

## 13. Limitations and Future Improvements

- Replace simulated dependency readiness with a real dependency check.
- Add Prometheus-compatible metrics.
- Improve structured application logging.
- Add container vulnerability scanning.
- Add deployment automation for a controlled production-like environment.

## 14. AI Assistance Disclosure

AI tools were used for learning support, troubleshooting guidance, documentation assistance, and reviewing implementation approaches.

The project implementation, command execution, testing, deployment, and verification were performed and reviewed by the author. Technical decisions and limitations were considered as part of the assessment.

## 15. Conclusion

This project demonstrates a practical DevOps workflow covering API development, automated testing, containerization, CI, health checks, versioned deployment, rollback, and operational documentation.
