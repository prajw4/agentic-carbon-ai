import pandas as pd

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from langchain_community.llms import HuggingFacePipeline
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate

# --------------------------------------------------
# Load local LLM (cached at module level by Docker)
# --------------------------------------------------
MODEL_NAME = "google/flan-t5-base"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

hf_pipeline = pipeline(
    "text2text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=150,
    temperature=0.5,
    do_sample=True,
    repetition_penalty=1.5
)

llm = HuggingFacePipeline(pipeline=hf_pipeline)

# --------------------------------------------------
# Load emissions data
# --------------------------------------------------
def load_emissions():
    return pd.read_csv("Data/emissions_data.csv")

# --------------------------------------------------
# Core analysis logic (FAST & DETERMINISTIC)
# --------------------------------------------------
def analyze_emissions_programmatically():
    df = load_emissions()

    high_emitters = df[df["CO2_Emissions_kg"] > 0.001]
    normal_emitters = df[df["CO2_Emissions_kg"] <= 0.001]

    analysis = []

    if not high_emitters.empty:
        models = ", ".join(high_emitters["Model"].tolist())
        analysis.append(
            f"The following models have high carbon emissions: {models}."
        )
        analysis.append(
            "These models consume more carbon due to higher computational complexity "
            "and larger workloads during execution."
        )

    if not normal_emitters.empty:
        analysis.append(
            "Other models demonstrate lower emissions because they use lighter "
            "architectures and more efficient processing."
        )

    analysis.append(
        "Carbon emissions can be reduced by applying techniques such as model pruning, "
        "quantization, efficient batching, and using energy-efficient hardware or "
        "renewable-powered infrastructure."
    )

    return " ".join(analysis)

# --------------------------------------------------
# Public API (DO NOT DECORATE)
# --------------------------------------------------
def run_carbon_agent():
    return analyze_emissions_programmatically()

__all__ = ["run_carbon_agent"]
