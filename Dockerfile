# -------------------------------
# Base image
# -------------------------------
FROM python:3.10-slim

# -------------------------------
# Environment variables
# -------------------------------
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app
ENV HF_HOME=/app/hf_cache
ENV TRANSFORMERS_CACHE=/app/hf_cache


# -------------------------------
# Working directory
# -------------------------------
WORKDIR /app

# -------------------------------
# System dependencies
# -------------------------------
RUN apt-get update && apt-get install -y \
    gcc \
    git \
    && rm -rf /var/lib/apt/lists/*

# -------------------------------
# Upgrade pip
# -------------------------------
RUN pip install --upgrade pip setuptools wheel

# -------------------------------
# Copy requirements first (cache-friendly)
# -------------------------------
COPY requirements.txt /app/requirements.txt

# -------------------------------
# Install Python dependencies
# -------------------------------
RUN pip install --no-cache-dir torch==2.2.2+cpu \
    -f https://download.pytorch.org/whl/torch_stable.html && \
    pip install --no-cache-dir -r requirements.txt

# -------------------------------
# Pre-download Hugging Face models (WEIGHTS ONLY)
# -------------------------------
RUN python - <<EOF
from transformers import pipeline

pipeline("sentiment-analysis")
pipeline("summarization", model="facebook/bart-large-cnn")
pipeline("question-answering", model="deepset/roberta-base-squad2")

print("Models cached successfully")
EOF

# -------------------------------
# Copy rest of the project
# -------------------------------
COPY . /app

# -------------------------------
# Expose Streamlit port
# -------------------------------
EXPOSE 8501

# -------------------------------
# Start Streamlit dashboard
# -------------------------------
CMD ["streamlit", "run", "Dashboard/dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
