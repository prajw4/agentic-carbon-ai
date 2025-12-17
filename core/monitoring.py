# core/monitoring.py

import time
import psutil
from prometheus_client import start_http_server, Gauge

# Define Prometheus metrics
cpu_usage_gauge = Gauge("cpu_usage_percent", "CPU Usage Percent")
ram_usage_gauge = Gauge("ram_usage_percent", "RAM Usage Percent")

def start_monitoring(port: int = 8000):
    """
    Starts Prometheus metrics server and updates CPU/RAM usage.
    This function is intended to be run in a background thread.
    """
    try:
        start_http_server(port)
        print(f"Prometheus monitoring server started on port {port}")
    except OSError:
        # Server already running (Streamlit rerun case)
        pass

    while True:
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent

        cpu_usage_gauge.set(cpu)
        ram_usage_gauge.set(ram)

        time.sleep(2)
