import streamlit as st
import pandas as pd
from prometheus_api_client import PrometheusConnect
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

prom = PrometheusConnect(url="http://localhost:8000", disable_ssl=True)

cpu_query = 'cpu_usage_percent'
ram_query = 'ram_usage_percent'

try:
    cpu_data = prom.get_current_metric_value(cpu_query)
    ram_data = prom.get_current_metric_value(ram_query)

    st.write(f"CPU Usage: {cpu_data[0]['value'][1]} %")
    st.write(f"RAM Usage: {ram_data[0]['value'][1]} %")

    fig, ax = plt.subplots()
    ax.bar(["CPU", "RAM"], [float(cpu_data[0]['value'][1]), float(ram_data[0]['value'][1])])
    ax.set_ylabel("Usage %")
    st.pyplot(fig)

except Exception as e:
    st.warning("Real-time metrics unavailable. Is monitoring.py running?")
