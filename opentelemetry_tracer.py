import os
from dotenv import load_dotenv
from opentelemetry.sdk.resources import Resource
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.trace import set_tracer_provider, get_tracer_provider
from opentelemetry.sdk.trace import TracerProvider, sampling
from opentelemetry.sdk.trace.export import BatchSpanProcessor


load_dotenv()

DT_API_URL = os.getenv("DT_API_URL")
DT_API_TOKEN = os.getenv("DT_API_TOKEN")


def init_tracer():
    resource = Resource.create({"service.name": "flask-dynatrace-app", "service.version": "1.0.0"})
    tracer_provider = TracerProvider(sampler=sampling.ALWAYS_ON, resource=resource)
    set_tracer_provider(tracer_provider)
    tracer_provider.add_span_processor(
        BatchSpanProcessor(
            OTLPSpanExporter(
                endpoint=f"{DT_API_URL}/v1/traces",
                headers={"Authorization": f"Api-Token {DT_API_TOKEN}"}
            )
        )
    )
