from flask import Flask, request
from time import time
import opentelemetry_tracer 
from opentelemetry.trace import get_tracer_provider
from opentelemetry import context

# Set up your Dynatrace API details

tracer = get_tracer_provider().get_tracer("flask-tracer")
app = Flask(__name__)

@app.before_request
def before_request():
    request.start_time = time()
    request.main_span = tracer.start_span("python-otel")
    request.main_span_ctx = context.attach(context.set_value("active_span", request.main_span))
    
    request.main_span.set_attribute("http.method", request.method)
    request.main_span.set_attribute("http.route", request.path)
    request.main_span.set_attribute("http.query_params", request.query_string.decode())
    request.main_span.set_attribute("http.user_agent", request.headers.get("User-Agent"))
    request.main_span.set_attribute("http.client_ip", request.remote_addr)
    request.main_span.set_attribute("environment", "production")
    request.main_span.set_attribute("service.version", "1.0.0")

@app.after_request
def after_request(response):
    if hasattr(request, 'main_span'):
        response_time = time() - request.start_time
        request.main_span.set_attribute("response_time_ms", response_time * 1000)
        request.main_span.set_attribute("http.status_code", response.status_code)
        request.main_span.end()
    context.detach(request.main_span_ctx)
    return response

@app.errorhandler(Exception)
def handle_exception(e):
    if hasattr(request, 'main_span'):
        request.main_span.set_attribute("error.message", str(e))
        request.main_span.set_attribute("error.type", type(e).__name__)
    return "An error occurred", 500

@app.route('/')
def home():
    return "Welcome to the Dynatrace Instrumented Flask App!"

@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    opentelemetry_tracer.init_tracer()
    app.run(debug=True)
