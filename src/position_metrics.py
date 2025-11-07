import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("/Users/maireadodwyer/Desktop/f1_winner_prediction/data/processed/f1_2025_results.csv")

df['GridPosition'] = df['GridPosition'].fillna(21)
df['Position'] = df['Position'].fillna(21)

positions = df['Position']

print(f"This is the total standard deviation of finishing positions : {positions.std()}")


driver_std = df.groupby("FullName")["Position"].std().reset_index()
driver_result_mean = df.groupby("FullName")["Position"].mean().reset_index()
driver_start_mean = df.groupby("FullName")["GridPosition"].mean().reset_index()

print("These are the standard deviations in a driver's finishing position \n")
print(f"{driver_std} \n")

print("These are the mean starting positions of the drivers \n")
print(f"{driver_start_mean} \n")

print("These are the mean finishing positions of the drivers \n")
print(f"{driver_result_mean} \n")