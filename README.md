# Dynatrax

**Dynatrax** is an observability solution that integrates OpenTelemetry with Dynatrace for a Python Flask application. It enables you to capture, track, and analyze traces, metrics, and logs in real-time, giving you deep insights into your application’s health and performance.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Setup and Installation](#setup-and-installation)
  - [Prerequisites](#prerequisites)
  - [Environment Variables](#environment-variables)
- [Project Structure](#project-structure)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [Generating Sample Traces and Metrics](#generating-sample-traces-and-metrics)
- [OpenTelemetry Configuration](#opentelemetry-configuration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction

Dynatrax provides an easy way to instrument a Flask application using OpenTelemetry and Dynatrace. By automatically exporting traces, metrics, and logs, Dynatrax enables in-depth observability for debugging and performance monitoring.

## Features

- **Tracing**: Tracks and visualizes the flow of requests through your application, giving insights into request paths and latencies.
- **Metrics**: Monitors and records key metrics to assess application health and performance.
- **Logging**: Provides structured logging, sent directly to Dynatrace, to support diagnostics and troubleshooting.

## Setup and Installation

Follow these steps to set up Dynatrax in your environment.

### Prerequisites

- Python 3.7+
- [Dynatrace account](https://www.dynatrace.com/), with access to create API tokens.
- Recommended: A virtual environment to isolate dependencies.

### Environment Variables

Dynatrax requires the following environment variables to communicate with Dynatrace:

- `DT_API_URL`: The base URL for Dynatrace API (e.g., `https://your-dynatrace-domain/api/v2/otlp`)
- `DT_API_TOKEN`: Your Dynatrace API token with the necessary scopes (ingest traces, metrics, logs).

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone 
   cd Dynatrax
   ```
2. **Setup virtualenv**:
    ```bash
    python3 -m venv .venv
    source .venv\bin\activate
    ```
2. **Install dependencies**:
    
   
    
    ```bash
    pip install -r requirements.txt
    ```
    
3. **Set up environment variables**: Configure your environment variables by creating a `.env` file or exporting them directly in the terminal.
    
    `.env` example:
    
    
    
    ```bash
    DT_API_URL=https://your-dynatrace-domain/api/v2/otlp
    DT_API_TOKEN=your_dynatrace_api_token
     ```
    
5. **Initialize OpenTelemetry components**:
    
    - Dynatrax uses OpenTelemetry SDKs for manual instrumentation of traces, metrics, and logs.
    [here](https://docs.dynatrace.com/docs/extend-dynatrace/opentelemetry/walkthroughs/python/python-manual)
    - Verify your `requirements.txt` includes necessary OpenTelemetry packages:
        `opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp-proto-http Flask`
        

## Project Structure


```
 Dynatrax/ 
    ├──  opentelemetry_tracer.py
    ├── app.py             # Main application file 
    ├── README.md          # Project documentation
    ├── requirements.txt   # Python dependencies 
    └── .env               # Environment variables (not included in repository) 
```

## Usage

### Running the Application

To run Dynatrax, execute the following command:

```
python app.py
```

The app should start on `http://localhost:5000`. You can visit this URL to generate sample traces and metrics.

### Generating Sample Traces and Metrics

Dynatrax includes sample endpoints for testing:

1. **`/` Endpoint**: The home route that triggers a simple trace.
2. **`/greet/<name>` Endpoint**: Greets the user by name and captures a custom trace with the user’s name.

Example:


```bash
curl http://localhost:5000/greet/John
```

This will generate a trace in Dynatrace showing the request path, response time, and any custom attributes.

## OpenTelemetry Configuration

OpenTelemetry settings are configured in `app.py`:

- **Tracing**: The `TracerProvider` and `BatchSpanProcessor` are initialized, and traces are sent to Dynatrace.
- **Metrics**: A `MeterProvider` is set up to capture basic metrics (e.g., request counts, durations).
- **Logging**: `LoggerProvider` enables sending structured logs directly to Dynatrace.


## Troubleshooting

1. **No Data in Dynatrace**:
    
    - Ensure that `DT_API_URL` and `DT_API_TOKEN` are correctly set and accessible.
    - Verify that your Dynatrace token has the necessary scopes: `metrics.ingest`, `logs.ingest`, `traces.ingest`.
      
2. **Connection Errors**:
    - Check that you’re using the correct API URL format: `https://<your_dynatrace_url>/api/v2/otlp`.
    - Confirm network connectivity from your application to Dynatrace.
    

## **Execution Summary**:




## TODO:

1) Send Logs to Dynatrace

## Contributing:

Contributions are welcome! Please fork the repository and submit a pull request.

## License:

Dynatrax is open-source and available under the MIT License. See `LICENSE` for details.
