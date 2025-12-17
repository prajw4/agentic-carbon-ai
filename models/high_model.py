# models/high_model.py
from transformers import pipeline
from codecarbon import EmissionsTracker
import pandas as pd
import os

CSV_PATH = os.path.join("Data", "emissions_data.csv")

def update_emissions_csv(model_name, co2_kg):
    if os.path.exists(CSV_PATH):
        df = pd.read_csv(CSV_PATH)
        if model_name in df['Model'].values:
            df.loc[df['Model'] == model_name, 'CO2_Emissions_kg'] = co2_kg
        else:
            df = pd.concat([df, pd.DataFrame([{'Model': model_name, 'CO2_Emissions_kg': co2_kg}])])
    else:
        df = pd.DataFrame([{'Model': model_name, 'CO2_Emissions_kg': co2_kg}])
    df.to_csv(CSV_PATH, index=False)

def run_high_carbon_model():
    tracker = EmissionsTracker(project_name="High_Carbon_QA_Model")
    tracker.start()

    qa_pipeline = pipeline("question-answering")
    sample_context = (
        "Agentic AI systems are transforming how autonomous decision-making is implemented "
        "in modern software. These systems can reason, plan, and take actions based on "
        "environmental feedback."
    )
    question = "How are Agentic AI systems transforming modern software?"
    result = qa_pipeline(question=question, context=sample_context)

    tracker.stop()
    co2_emitted = tracker.final_emissions
    update_emissions_csv("High Carbon QA Model", co2_emitted)
    return {"model": "High Carbon QA Model", "result": result, "co2_kg": co2_emitted}

if __name__ == "__main__":
    print(run_high_carbon_model())
