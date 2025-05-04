"""Python template for new projects."""

from opentelemetry import trace, metrics
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter
from opentelemetry.sdk.metrics.export import ConsoleMetricExporter, PeriodicExportingMetricReader
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
import logging
from opentelemetry.instrumentation.logging import LoggingInstrumentor
from fastapi import FastAPI
from opentelemetry.metrics import CallbackOptions

# Set up tracing
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)
span_processor = SimpleSpanProcessor(ConsoleSpanExporter())
trace.get_tracer_provider().add_span_processor(span_processor)

# Set up metrics
metrics.set_meter_provider(MeterProvider(
    metric_readers=[
        PeriodicExportingMetricReader(ConsoleMetricExporter())
    ]
))
meter = metrics.get_meter(__name__)
counter = meter.create_counter("example_counter", description="An example counter")

# Create a gauge metric
gauge = meter.create_observable_gauge(
    "example_gauge",
    description="An example gauge",
    callbacks=[]
)

def set_gauge(value: float):
    """Set the gauge value."""
    def callback(options: CallbackOptions):
        yield value
    gauge.callbacks.clear()
    gauge.callbacks.append(callback)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
LoggingInstrumentor().instrument(set_logging_format=True)

# Initialize FastAPI app
app = FastAPI()

@app.get("/log/{level}")
def log_message(level: str):
    """Log a message at the specified level."""
    message = f"Log message at {level} level"
    if level.lower() == "info":
        logger.info(message)
    elif level.lower() == "debug":
        logger.debug(message)
    elif level.lower() == "warning":
        logger.warning(message)
    elif level.lower() == "error":
        logger.error(message)
    elif level.lower() == "critical":
        logger.critical(message)
    else:
        return {"error": "Invalid log level"}
    return {"message": message}

@app.get("/increment")
def increment_counter():
    """Increment the counter metric."""
    counter.add(1, {"operation": "increment"})
    return {"message": "Counter incremented"}

@app.get("/set_gauge")
def update_gauge(value: float):
    """Set the gauge metric to the specified value."""
    set_gauge(value)
    return {"message": f"Gauge set to {value}"}
