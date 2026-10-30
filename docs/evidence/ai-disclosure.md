# AI Assistance Disclosure

## 1. Purpose

This document provides a transparent account of how AI assistance was used during the development of the Apex Operations API assessment project.

AI was used as a productivity and learning aid to reduce repetitive scripting time, understand technical concepts, troubleshoot issues, and improve project documentation.

The project was not completed by relying entirely on AI-generated output. I actively worked on implementation, executed commands, investigated errors, tested application behavior, and verified deployment results.

## 2. How AI Assistance Was Used

I used ChatGPT as a technical assistant in the following areas:

### Python and FastAPI scripting

- Obtained assistance with an initial FastAPI application implementation to save scripting time.
- Used AI explanations to understand the API structure, routes, environment variables, health checks, readiness behavior, and application logging.
- Reviewed and understood the generated code before using and testing it.

### Docker and containerization

- Received guidance on Dockerfile structure, image versioning, container configuration, and non-root execution.
- Used explanations to understand Docker build arguments, environment variables, and container health checks.

### CI and automated testing

- Received assistance understanding GitHub Actions workflow configuration.
- Used guidance for setting up Ruff and Pytest checks and interpreting test results.

### Documentation

- Used AI assistance to structure and prepare documentation covering architecture, deployment procedures, technical decisions, and operational practices.
- Reviewed the documentation against the actual project implementation and its limitations.

## 3. Work Personally Performed

I personally carried out and verified substantial parts of the project, including:

- Setting up and working in the AWS EC2 Amazon Linux environment.
- Creating and managing the project repository using Git and GitHub.
- Installing and configuring the required development tools.
- Building Docker images and deploying the application using Docker Compose.
- Investigating and resolving the Docker Buildx compatibility issue by using explicit Docker builds and Compose deployment without rebuilding.
- Executing automated tests and Ruff checks.
- Demonstrating an intentional test failure and restoring the passing test suite.
- Deploying application version `1.0.1` and verifying its behavior.
- Performing a rollback to version `1.0.0` and verifying application health.
- Collecting and committing deployment and testing evidence.
- Reviewing application responses, container status, and deployment behavior.

These activities involved hands-on command execution, observation, troubleshooting, and verification in my assessment environment.

## 4. My Approach to AI-Generated Code

When AI provided code or configuration examples, I treated them as assistance rather than blindly accepting them.

My approach was to:

1. Understand the purpose of the suggested code.
2. Review how the different components work together.
3. Execute the implementation in my environment.
4. Investigate errors and unexpected behavior.
5. Verify the output through tests, API requests, and container checks.
6. Retain awareness of limitations and areas that could be improved.

AI assistance helped reduce the time spent writing repetitive code and documentation, allowing me to dedicate more time to hands-on implementation and troubleshooting.

## 5. Limitations and Responsibility

AI-generated suggestions can contain errors or assumptions that do not match the actual environment.

I therefore treated AI responses as guidance and verified important implementation and deployment results myself.

I remain responsible for understanding the submitted project, explaining its technical decisions, and discussing its limitations during assessment or interview discussions.

## 6. Final Statement

I used ChatGPT as a productivity tool, learning companion, and troubleshooting assistant during this assessment.

Although I received assistance with the initial FastAPI scripting, technical explanations, selected configuration examples, and documentation, I personally worked through the environment setup, command execution, testing, deployment, version rollback, and verification.

My objective was not simply to produce a working project, but to understand the DevOps workflow and gain practical experience through hands-on implementation.

**AI assistance supported my work; it did not replace my responsibility for understanding, executing, and validating the project.**
