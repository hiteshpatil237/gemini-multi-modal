from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

population_path = os.path.join("population.csv")
population_df = pd.read_csv(population_path)

print(population_df.head())