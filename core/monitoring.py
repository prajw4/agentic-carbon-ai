import time
import psutil
from prometheus_client import start_http_server, Gauge

# Start Prometheus metrics server on port 8000
start_http_server(8000)

# Define metrics
cpu_usage_gauge = Gauge('cpu_usage_percent', 'CPU Usage Percent')
ram_usage_gauge = Gauge('ram_usage_percent', 'RAM Usage Percent')

print("Prometheus monitoring server started on port 8000")

try:
    while True:
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent

        cpu_usage_gauge.set(cpu)
        ram_usage_gauge.set(ram)

        print(f"CPU: {cpu}% | RAM: {ram}%")
        time.sleep(2)

except KeyboardInterrupt:
    print("Monitoring stopped.")
