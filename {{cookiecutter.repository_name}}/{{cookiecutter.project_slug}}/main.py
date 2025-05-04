"""Python template for new projects."""

from fastapi import FastAPI
from prometheus_client import make_asgi_app
from starlette.middleware.wsgi import WSGIMiddleware
from {{cookiecutter.project_slug}}.routes import log_routes, metrics_routes

# Initialize FastAPI app
app = FastAPI()

# Include routes
app.include_router(log_routes.router)
app.include_router(metrics_routes.router)

# Prometheus metrics endpoint
prometheus_app = make_asgi_app()
app.mount("/metrics", WSGIMiddleware(prometheus_app))
