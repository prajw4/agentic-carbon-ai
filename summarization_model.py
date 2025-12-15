from transformers import pipeline
from codecarbon import EmissionsTracker
import pandas as pd
import os

# Start carbon emission tracking
tracker = EmissionsTracker(project_name="Text_Summarization")
tracker.start()

# Load summarization model
summarizer = pipeline("summarization")

# Sample business document
text = """
Artificial Intelligence is transforming businesses by automating processes,
improving decision-making, and enhancing customer experiences.
However, larger AI models consume more compute resources, leading to higher
energy usage and increased carbon emissions.
"""

# Run summarization model
summary = summarizer(text, max_length=50, min_length=25, do_sample=False)

# Stop tracking
emissions = tracker.stop()

# Save or append emission data
file_path = "emissions_data.csv"

new_data = pd.DataFrame({
    "Model": ["Text Summarization"],
    "CO2_Emissions_kg": [emissions]
})

if os.path.exists(file_path):
    old_data = pd.read_csv(file_path)
    final_data = pd.concat([old_data, new_data])
else:
    final_data = new_data

final_data.to_csv(file_path, index=False)

print("Summary Output:", summary)
print("CO2 Emissions (kg):", emissions)
