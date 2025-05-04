from fastapi import APIRouter, Query
from prometheus_client import Counter, Gauge

router = APIRouter()

# Prometheus metrics
counter = Counter("example_counter", "An example counter")
gauge = Gauge("example_gauge", "An example gauge")

@router.get("/increment")
def increment_counter():
    """Increment the counter metric."""
    counter.inc()
    return {"message": "Counter incremented"}

@router.get("/set_gauge")
def update_gauge(value: float = Query(..., description="Value to set the gauge to")):
    """Set the gauge metric to the specified value."""
    gauge.set(value)
    return {"message": f"Gauge set to {value}"}