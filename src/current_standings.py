import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("/Users/maireadodwyer/Desktop/f1_winner_prediction/data/processed/f1_2025_results.csv")

df.sort_values(df.columns[2],
               axis = 0,
               inplace = True)

total_points = df['Points'].groupby(df['DriverId'])

points = total_points.sum()

standings = (
    total_points
    .sum()
    .sort_values(ascending=False)
    .reset_index(name="points")
)

print(standings.to_string(index=False))