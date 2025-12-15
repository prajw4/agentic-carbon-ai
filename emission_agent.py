import pandas as pd

class CarbonEmissionAgent:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def observe(self):
        # Read emissions data
        self.data = pd.read_csv(self.csv_file)
        print("\n[AGENT] Observing emission data...\n")
        print(self.data)

    def analyze(self):
        # Identify the model with highest emissions
        self.highest_emission = self.data.loc[
            self.data["CO2_Emissions_kg"].idxmax()
        ]
        print("\n[AGENT] Analyzing data...\n")
        print("Highest emission model:", self.highest_emission["Model"])

    def decide(self):
        emission_value = self.highest_emission["CO2_Emissions_kg"]

        if emission_value > 0.001:
            self.recommendation = (
                "High carbon footprint detected. "
                "Recommendation: Run this model during off-peak hours "
                "or switch to a smaller/distilled model."
            )
        else:
            self.recommendation = (
                "Carbon footprint is within acceptable limits."
            )

    def act(self):
        print("\n[AGENT] Action (Recommendation):\n")
        print(self.recommendation)


if __name__ == "__main__":
    agent = CarbonEmissionAgent("emissions_data.csv")
    agent.observe()
    agent.analyze()
    agent.decide()
    agent.act()
