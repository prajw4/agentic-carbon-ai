# 🌱 Agentic AI: Carbon Footprint & Resource Monitoring Dashboard

## 📌 Project Overview

This project is a Dockerized, agent-driven AI sustainability dashboard that analyzes the carbon footprint of AI workloads and monitors real-time system resource usage.

It helps developers and organizations understand the environmental impact of AI models, receive intelligent sustainability recommendations, and monitor system performance in a single interactive interface. The entire application is containerized using Docker for easy setup, reproducibility, and interview-ready demonstrations.

---

## ✨ Key Features

### 🌿 Carbon Emissions Analysis
- Tracks CO₂ emissions for multiple AI tasks:
  - Sentiment Analysis
  - Text Summarization
  - Question Answering
- Displays emissions using interactive bar charts.
- Identifies high-emission models dynamically based on runtime data rather than hardcoded labels.

---

### 🤖 Agentic AI Insights
- Uses an AI agent built with LangChain and a local Hugging Face model (Flan-T5).
- Analyzes emission data programmatically and generates sustainability recommendations.
- Suggests optimization strategies such as:
  - Using smaller or distilled models
  - Running workloads during off-peak hours
  - Applying pruning and quantization techniques
- Agent output is cached to ensure fast dashboard interaction.

---

### 💻 Real-time CPU & RAM Monitoring
- Tracks live CPU and memory usage using psutil and Prometheus.
- Displays real-time metrics directly in the dashboard.
- Monitoring runs automatically in the background when the application starts.

---

### 🎨 Interactive Streamlit Dashboard
- Clean and minimal user interface built with Streamlit.
- Optimized with caching for fast load times and smooth interaction.
- Designed for demos, evaluations, and technical interviews.

---

## 🛠️ Tech Stack

- Python – Core application logic
- Streamlit – Interactive dashboard UI
- Pandas – Data processing
- Matplotlib – Data visualization
- CodeCarbon – Carbon emission tracking
- LangChain – AI agent orchestration
- Transformers (Hugging Face) – Local LLM (Flan-T5)
- Prometheus & psutil – Real-time CPU/RAM monitoring
- Docker – Containerization and deployment

---

## 📂 Project Structure

C:.
│   .gitignore
│   Dockerfile
│   emissions.csv
│   emissions.csv.bak
│   README.md
│   requirements.txt
│
├── agents
│   ├── carbon_agent.py        # AI agent logic for sustainability insights
│   └── __init__.py
│
├── core
│   └── monitoring.py          # Prometheus-based CPU/RAM monitoring
│
├── Dashboard
│   └── dashboard.py           # Streamlit dashboard UI
│
├── Data
│   ├── emissions.csv
│   ├── emissions.csv.bak
│   └── emissions_data.csv     # Carbon emission dataset
│
└── models
    ├── sentiment_model.py     # Sentiment analysis model
    ├── summarization_model.py # Text summarization model
    └── high_model.py          # Question answering / third model

---

## 🐳 Docker Usage

# Docker Hub Repository :-

The Docker image for this project is publicly available on Docker Hub:

https://hub.docker.com/r/prajwal1504/carbon-ai-dashboard



### Pull & Run from Docker Hub

docker pull prajwal1504/carbon-ai-dashboard:latest
docker run -p 8501:8501 prajwal1504/carbon-ai-dashboard:latest

Then open the dashboard at:
http://localhost:8501

---

### Build & Run Locally (Optional)

git clone https://github.com/prajwal1504/agentic-corbon-ai.git
cd agentic-corbon-ai

docker build -t carbon-ai-dashboard .
docker run -p 8501:8501 carbon-ai-dashboard

---

## 📊 Dashboard Output

- Carbon Emissions: Bar chart comparing emissions across AI tasks
- Agent Insights: AI-generated sustainability recommendations
- CPU & RAM Usage: Live system performance metrics

---

## ⚠️ Important Notes

- Carbon emissions depend on runtime behavior and system resources, not model names.
- CPU and RAM metrics reflect the host system where Docker is running.
- Initial AI agent execution may take a few seconds due to model inference.

---

## 🌟 Future Enhancements

- Historical carbon emission trends
- Automated alerts for high-emission workloads
- Kubernetes-based deployment for scalability
- Cloud integration (AWS, GCP, Azure)

---

## 🎓 Summary

This project analyzes the carbon footprint of AI workloads, monitors real-time system resources, and provides AI-driven sustainability insights through a Dockerized Streamlit dashboard designed for reproducibility and easy evaluation.
