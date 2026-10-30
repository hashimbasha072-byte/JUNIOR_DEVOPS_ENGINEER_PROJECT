# Apex Operations API — Technical Decision Memo

## 1. Objective

This document explains the technical choices made while implementing the Apex Operations API assessment project.

The main priorities were simplicity, reproducibility, maintainability, security, and clear operational procedures.

## 2. Technology Decisions

| Technology | Decision | Reason |
|---|---|---|
| Python | Use Python for application development | Simple and widely used for automation and APIs |
| FastAPI | Use FastAPI as the API framework | Lightweight, modern, and supports automatic API documentation |
| Uvicorn | Use Uvicorn as the application server | ASGI server suitable for running FastAPI |
| Docker | Package the application in a container | Consistent application runtime across environments |
| Docker Compose | Manage the application container | Simple deployment and configuration for a single-service project |
| Pytest | Automate application tests | Readable and maintainable test cases |
| Ruff | Perform Python code quality checks | Fast linting and consistent code quality |
| GitHub Actions | Automate CI checks | Integrates directly with the GitHub repository |

## 3. Container Design

A Docker image based on `python:3.12-slim` was selected to provide a lightweight Python runtime.

The container runs the application using a dedicated non-root user rather than the default root user.

Application dependencies are pinned in `requirements.txt` to improve reproducibility.

## 4. Deployment Strategy

Docker Compose was selected instead of Kubernetes because this assessment uses a single API service and does not require multi-container orchestration or cluster management.

The application image is versioned so that a previous release can be selected during rollback.

The `APP_VERSION` environment variable controls which versioned image Docker Compose uses.

## 5. CI Strategy

GitHub Actions was selected to automate basic quality and build verification.

The workflow executes:

1. Python setup and dependency installation.
2. Ruff linting.
3. Pytest automated tests.
4. Docker image build verification.

This helps detect common code and build problems before deployment.

## 6. Health and Readiness Design

The `/health` endpoint reports whether the application is responding.

The `/ready` endpoint demonstrates readiness behavior using a configurable dependency-availability environment variable.

This implementation is intentionally simple. A production system should check the actual availability of its critical dependencies.

## 7. Security Decisions

- Run the application as a non-root container user.
- Use a slim base image.
- Keep the current host port binding on localhost.
- Avoid storing credentials in source code.
- Pin application dependencies.

Additional production controls such as image vulnerability scanning, secrets management, and network restrictions would be valuable future improvements.

## 8. Limitations and Trade-offs

| Area | Current implementation | Possible improvement |
|---|---|---|
| Readiness | Simulated dependency availability | Real dependency health checks |
| Metrics | JSON diagnostic endpoint | Prometheus-compatible metrics |
| Logging | Request information in application logs | Valid structured JSON logging |
| Deployment | Single-host Docker Compose | Controlled automated deployment |
| Security | Non-root user and slim image | Vulnerability scanning and additional hardening |

## 9. Conclusion

The selected architecture keeps the assessment project small and reproducible while demonstrating essential DevOps practices.

The implementation prioritizes understanding, operational visibility, automated verification, and safe version rollback over introducing unnecessary infrastructure complexity.
