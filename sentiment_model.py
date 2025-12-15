from transformers import pipeline
from codecarbon import EmissionsTracker
import pandas as pd

# Start tracking carbon emissions
tracker = EmissionsTracker(project_name="Sentiment_Analysis")
tracker.start()

# Load sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis")

# Sample business text
text = "The customer support was extremely helpful and fast."

# Run model
result = sentiment_analyzer(text)

# Stop tracking
emissions = tracker.stop()

# Save results to CSV
data = {
    "Model": ["Sentiment Analysis"],
    "CO2_Emissions_kg": [emissions]
}

df = pd.DataFrame(data)
df.to_csv("emissions_data.csv", index=False)

print("Sentiment Result:", result)
print("CO2 Emissions (kg):", emissions)
