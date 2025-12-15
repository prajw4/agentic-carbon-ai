# \\ud83c\\udf31 Agentic AI: Carbon Footprint Dashboard for AI Models

## \\ud83d\\udccc Project Overview

This project is an interactive Streamlit dashboard designed to help businesses:

- \\ud83c\\udf0d Monitor the carbon footprint of their AI models
- \\ud83e\\udd16 Get agent recommendations
- \\ud83d\\udcca Track real-time system performance metrics (CPU and RAM usage)

The dashboard is eco-friendly, interactive, and visually appealing, providing actionable insights to reduce energy consumption and CO\\u2082 emissions.

---

## \\u2728 Features

### \\ud83c\\udf3f Carbon Emissions Monitoring

- Tracks per-model CO\\u2082 emissions for AI models like sentiment analysis and text summarization.
- Displays bar charts showing emissions for each model.
- Highlights highest-emission models to identify energy-intensive workflows.

### \\ud83e\\udd16 Agent Recommendations

- Automatically provides actionable recommendations for high-emission models.
- Suggests running jobs during off-peak hours or using smaller/distilled models.
- Shows recommendations interactively on the dashboard.

### \\ud83d\\udcbb Real-time CPU and RAM Monitoring

- Tracks live CPU and RAM usage using Prometheus.
- Displays metrics and visual charts for easy monitoring.
- Helps optimize AI workloads and system performance.

### \\ud83c\\udfa8 Interactive & Minimal Dashboard

- Dashboard background has a fade-themed gradient, giving it a professional look.

---

## \\ud83d\\udd20\\ufe0f Technical Stack

- **Python** \\u2013 Backend logic and data processing
- **Streamlit** \\u2013 Interactive dashboard UI
- **Pandas** \\u2013 Data handling
- **Matplotlib** \\u2013 Charts and visualization
- **CodeCarbon** \\u2013 CO\\u2082 emissions tracking
- **Prometheus** \\u2013 Real-time CPU/RAM metrics
- **Requests** \\u2013 Fetching Prometheus metrics
- **Streamlit Session State** \\u2013 Managing interactive UI

---

## \\ud83d\\uddc2 Project Structure

```
agentic-carbon-ai/
│
├\\u2500 dashboard.py         # \\ud83c\\udf1f Main Streamlit dashboard with interactive cards
├\\u2500 monitoring.py        # \\ud83d\\udce1 Prometheus exporter for CPU/RAM metrics
├\\u2500 emissions_data.csv   # \\ud83d\\uddde Sample data for AI model emissions
├\\u2500 README.md            # \\ud83d\\udcd6 Project documentation
\\u2514\\u2500 requirements.txt     # \\ud83d\\udcc6 Required Python packages
```

---

## \\ud83d\\ude80 How to Run the Project

### Clone the repository:

```bash
git clone https://github.com/<your-username>/agentic-carbon-ai.git
cd agentic-carbon-ai
```

### Install required packages:

```bash
pip install -r requirements.txt
```

### Start the Prometheus monitoring server (for real-time CPU/RAM metrics):

```bash
python monitoring.py
```

### Run the Streamlit dashboard:

```bash
streamlit run dashboard.py
```

### Interact with the dashboard:

- \\ud83d\\udd39 **Carbon Emissions**: Click to view per-model CO\\u2082 charts.
- \\ud83d\\udd39 **Agent Recommendations**: Click to see suggested actions.
- \\ud83d\\udd39 **Real-time CPU/RAM**: Click to monitor system metrics live.

---

## \\ud83d\\udcca Sample Output

- **Carbon Emissions**: Bar chart showing CO\\u2082 emission per model.
- **Agent Recommendations**: Shows high-emission models and recommendations.
- **Real-time CPU/RAM**: Metrics displayed as live numbers and bar charts.

---

## \\u26a0\\ufe0f Notes

- Ensure `monitoring.py` is running before viewing real-time CPU/RAM metrics.
- CSV data (`emissions_data.csv`) is used for sample emissions\\u2014replace with your models for actual data.
- Dashboard is interactive, with hover effects and fade-themed background.

---

## \\ud83c\\udf1f Future Enhancements

- \\ud83d\\udd39 Automate carbon-saving actions based on agent recommendations.
- \\ud83d\\udd39 Integrate with Kubernetes or AWS/Azure for workflow scaling.
- \\ud83d\\udd39 Add historical trends and alerts for high-energy models.