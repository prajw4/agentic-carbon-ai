# 🌱 Agentic AI: Carbon Footprint Dashboard for AI Models

## 📌 Project Overview

This project is an interactive Streamlit dashboard designed to help businesses:

- 🌍 Monitor the carbon footprint of their AI models
- 🤖 Get agent recommendations
- 📊 Track real-time system performance metrics (CPU and RAM usage)

The dashboard is eco-friendly, interactive, and visually appealing, providing actionable insights to reduce energy consumption and CO₂ emissions.

---

## ✨ Features

### 🌿 Carbon Emissions Monitoring

- Tracks per-model CO₂ emissions for AI models like sentiment analysis and text summarization.
- Displays bar charts showing emissions for each model.
- Highlights highest-emission models to identify energy-intensive workflows.

### 🤖 Agent Recommendations

- Automatically provides actionable recommendations for high-emission models.
- Suggests running jobs during off-peak hours or using smaller/distilled models.
- Shows recommendations interactively on the dashboard.

### 💻 Real-time CPU and RAM Monitoring

- Tracks live CPU and RAM usage using Prometheus.
- Displays metrics and visual charts for easy monitoring.
- Helps optimize AI workloads and system performance.

### 🎨 Interactive & Minimal Dashboard

- Dashboard background has a fade-themed gradient, giving it a professional look.

## 🛠️ Technical Stack

- **Python** – Backend logic and data processing
- **Streamlit** – Interactive dashboard UI
- **Pandas** – Data handling
- **Matplotlib** – Charts and visualization
- **CodeCarbon** – CO₂ emissions tracking
- **Prometheus** – Real-time CPU/RAM metrics
- **Requests** – Fetching Prometheus metrics
- **Streamlit Session State** – Managing interactive UI

---

## 📂 Project Structure

```
agentic-corbon-ai/
│
├─ dashboard.py         # 🌟 Main Streamlit dashboard with interactive cards
├─ monitoring.py        # 📡 Prometheus exporter for CPU/RAM metrics
├─ emissions_data.csv   # 📝 Sample data for AI model emissions
├─ README.md            # 📖 Project documentation
└─ requirements.txt     # 📦 Required Python packages
```

### 🚀 How to Run the Project

1. **Clone the repository**:
    ```bash
    git clone https://github.com/<your-username>/agentic-corbon-ai.git
    cd agentic-corbon-ai
    ```

2. **Install required packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Start the Prometheus monitoring server** (for real-time CPU/RAM metrics):
    ```bash
    python monitoring.py
    ```

4. **Run the Streamlit dashboard**:
    ```bash
    streamlit run dashboard.py
    ```

5. **Interact with the dashboard**:
    - 🔹 **Carbon Emissions**: Click to view per-model CO₂ charts.
    - 🔹 **Agent Recommendations**: Click to see suggested actions.
    - 🔹 **Real-time CPU/RAM**: Click to monitor system metrics live.

## 📊 Sample Output

- **Carbon Emissions**: Bar chart showing CO₂ emission per model.
- **Agent Recommendations**: Shows high-emission models and recommendations.
- **Real-time CPU/RAM**: Metrics displayed as live numbers and bar charts.

⚠️ **Notes**
- Ensure `monitoring.py` is running before viewing real-time CPU/RAM metrics.
- Sample CSV data (`emissions_data.csv`) is used for emissions—replace with your models for actual data.
- Dashboard is interactive, with hover effects and fade-themed background.

🌟 **Future Enhancements**
- 🔹 Automate carbon-saving actions based on agent recommendations.
- 🔹 Integrate with Kubernetes or AWS/Azure for workflow scaling.
- 🔹 Add historical trends and alerts for high-energy models.

