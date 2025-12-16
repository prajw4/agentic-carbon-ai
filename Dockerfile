# Use lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit and Prometheus ports
EXPOSE 8501
EXPOSE 8000

# Run both monitoring and dashboard
CMD python monitoring.py & streamlit run dashboard.py --server.port=8501 --server.address=0.0.0.0
