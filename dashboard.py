import streamlit as st
import pandas as pd
import requests
import streamlit.components.v1 as components
import matplotlib.pyplot as plt

# Title
st.title("Agentic AI Carbon & Resource Dashboard")

# Section 1: Carbon Emissions per Model
st.header("1️⃣ Carbon Emissions")
df = pd.read_csv("emissions_data.csv")
st.dataframe(df)

# Bar chart
st.bar_chart(df.set_index("Model"))

# Section 2: Agent Recommendations
st.header("2️⃣ Agent Recommendations")

highest_emission = df.loc[df["CO2_Emissions_kg"].idxmax()]
if highest_emission["CO2_Emissions_kg"] > 0.001:
    st.success(
        f"High carbon footprint detected for {highest_emission['Model']}.\n"
        "Recommendation: Run during off-peak hours or use a smaller model."
    )
else:
    st.info("All models are within acceptable carbon limits.")

# Section 3: Real-time Resource Usage
st.header("3️⃣ Real-time CPU/RAM Usage (Last 1 min)")

# Fetch Prometheus exporter text metrics directly from the monitoring exporter
REFRESH_SECONDS = 5
PROM_METRICS_URL = "http://localhost:8000"  # monitoring.py uses start_http_server(8000)

def parse_prometheus_text_metrics(text):
    cpu = None
    ram = None
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("cpu_usage_percent"):
            parts = line.split()
            if len(parts) >= 2:
                try:
                    cpu = float(parts[-1])
                except ValueError:
                    cpu = None
        elif line.startswith("ram_usage_percent"):
            parts = line.split()
            if len(parts) >= 2:
                try:
                    ram = float(parts[-1])
                except ValueError:
                    ram = None
    return cpu, ram

def fetch_metrics(url):
    try:
        resp = requests.get(url, timeout=2)
        resp.raise_for_status()
        cpu, ram = parse_prometheus_text_metrics(resp.text)
        # some exporters expose at /metrics; try fallback if needed
        if (cpu is None or ram is None) and url.endswith("/") is False:
            # try /metrics
            try:
                resp2 = requests.get(url.rstrip('/') + '/metrics', timeout=2)
                resp2.raise_for_status()
                cpu2, ram2 = parse_prometheus_text_metrics(resp2.text)
                cpu = cpu or cpu2
                ram = ram or ram2
            except Exception:
                pass
        if cpu is None or ram is None:
            raise RuntimeError("Required metrics not found in response.")
        return cpu, ram, None
    except Exception as e:
        return None, None, str(e)

cpu_val, ram_val, error = fetch_metrics(PROM_METRICS_URL)

if error:
    st.warning("Real-time metrics unavailable. Is monitoring.py running?")
    with st.expander("Metrics fetch details"):
        st.write(error)
else:
    col_cpu, col_ram = st.columns(2)
    col_cpu.metric("CPU Usage (%)", f"{cpu_val:.1f} %")
    col_ram.metric("RAM Usage (%)", f"{ram_val:.1f} %")

# lightweight auto-refresh: reload the page every REFRESH_SECONDS seconds
js = f"""
<script>
if (!window.__streamlit_autoreload_set) {{
  window.__streamlit_autoreload_set = true;
  setTimeout(function() {{ window.location.reload(); }}, {REFRESH_SECONDS * 1000});
}}
</script>
"""
components.html(js, height=0)
