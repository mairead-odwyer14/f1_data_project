#Program to investigate correlation between qualifying position and race result using pearson method
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("/Users/maireadodwyer/Desktop/f1_winner_prediction/data/processed/f1_2025_results.csv")

df['GridPosition'] = df['GridPosition'].fillna(21)
df['Position'] = df['Position'].fillna(21)

print("This is a program to find the correlation between qualifying position and race result")

correlation = np.corrcoef(df['GridPosition'], df['Position'])

print(correlation)

if (correlation[1][0] >= 0.9 and correlation[1][0] <= 1) or (correlation[1][0] <= -1 and correlation[1][0] >= -0.9):
    print("There is a very strong correlation between qualifying position and race result")
elif (correlation[1][0] >= 0.5 and correlation[1][0] < 0.9) or (correlation[1][0] <= -0.5 and correlation[1][0] > -0.9):
    print("There is a strong correlation between qualifying position and race result")
elif (correlation[1][0] > 0 and correlation[1][0] < 0.5) or (correlation[1][0] < 0 and correlation[1][0] > -0.5):
    print("There is a weak correlation between qualifying position and race result")
else:
    print("There is no correlation between qualifying position and race result")