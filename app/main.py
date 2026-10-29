import logging
import os

from fastapi import FastAPI, HTTPException, Request

logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format="%(message)s",
)
logger = logging.getLogger("apex-api")

APP_VERSION = os.getenv("APP_VERSION", "0.1.0")
DEPENDENCY_AVAILABLE = (
    os.getenv("DEPENDENCY_AVAILABLE", "true").lower() == "true"
)

app = FastAPI(
    title="Apex Operations API",
    version=APP_VERSION,
)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    response = await call_next(request)
    logger.info(
        '{"event":"http_request","method":"%s",'
        '"path":"%s","status_code":%s}',
        request.method,
        request.url.path,
        response.status_code,
    )
    return response


@app.get("/")
def root():
    return {
        "application": "Apex Operations API",
        "version": APP_VERSION,
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/ready")
def readiness():
    if not DEPENDENCY_AVAILABLE:
        raise HTTPException(
            status_code=503,
            detail="Dependency unavailable",
        )
    return {"status": "ready"}


@app.get("/metrics")
def metrics():
    return {
        "application_version": APP_VERSION,
        "dependency_available": DEPENDENCY_AVAILABLE,
    }
