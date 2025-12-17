import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
import os
import threading

from core.monitoring import start_monitoring

# ------------------ Page Config ------------------
st.set_page_config(
    page_title="Agentic AI Carbon Dashboard",
    layout="wide"
)

# ------------------ Start Monitoring (ONCE) ------------------
if "monitoring_started" not in st.session_state:
    monitoring_thread = threading.Thread(
        target=start_monitoring,
        kwargs={"port": 8000},
        daemon=True
    )
    monitoring_thread.start()
    st.session_state.monitoring_started = True

# ------------------ Cached CSV Loader ------------------
@st.cache_data
def load_emissions_data(path):
    return pd.read_csv(path)

# ------------------ Title ------------------
st.title("Agentic AI Carbon & Resource Dashboard")

# ------------------ Section 1: Carbon Emissions ------------------
st.header("1️⃣ Carbon Emissions")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "Data", "emissions_data.csv")
df = load_emissions_data(DATA_PATH)

st.bar_chart(df.set_index("Model"))

st.markdown("---")

# ------------------ Section 2: Agent Recommendations ------------------
st.header("2️⃣ Agent Recommendations")

highest_emission = df.loc[df["CO2_Emissions_kg"].idxmax()]
if highest_emission["CO2_Emissions_kg"] > 0.001:
    st.success(
        f"High carbon footprint detected for {highest_emission['Model']}.\n"
        "Recommendation: Run during off-peak hours or use a smaller model."
    )
else:
    st.info("All models are within acceptable carbon limits.")

st.markdown("---")

# ------------------ Section 3: Real-time CPU/RAM Usage ------------------
st.header("3️⃣ Real-time CPU/RAM Usage")

PROM_METRICS_URL = "http://localhost:8000/metrics"

def parse_prometheus_text_metrics(text):
    cpu = None
    ram = None
    for line in text.splitlines():
        if line.startswith("cpu_usage_percent"):
            cpu = float(line.split()[-1])
        elif line.startswith("ram_usage_percent"):
            ram = float(line.split()[-1])
    return cpu, ram

def fetch_metrics():
    try:
        resp = requests.get(PROM_METRICS_URL, timeout=2)
        resp.raise_for_status()
        cpu, ram = parse_prometheus_text_metrics(resp.text)
        if cpu is None or ram is None:
            raise RuntimeError("Metrics not yet available")
        return cpu, ram, None
    except Exception as e:
        return None, None, str(e)

cpu_val, ram_val, error = fetch_metrics()

if error:
    st.warning("Real-time metrics initializing…")
else:
    col1, col2 = st.columns(2)
    col1.metric("CPU Usage (%)", f"{cpu_val:.1f}")
    col2.metric("RAM Usage (%)", f"{ram_val:.1f}")

st.markdown("---")

# ------------------ Section 4: LangChain Agent Insights ------------------
st.header("4️⃣ LangChain Agent Insights")

@st.cache_data(show_spinner="Generating sustainability insights...")
def get_cached_agent_insight():
    from agents.carbon_agent import run_carbon_agent
    return run_carbon_agent()

if st.button("Run AI Agent"):
    insight = get_cached_agent_insight()
    st.text(insight)

