#Program to see a driver's positions from qualifying to race result
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("/Users/maireadodwyer/Desktop/f1_winner_prediction/data/processed/f1_2025_results.csv")

driver_names = np.array(df['FullName'].unique())
print("Enter one of the following names: ")
for i in range(0,len(driver_names)):
    print(f"{driver_names[i]} \n")

chosen = input()

filtered_df = df.loc[df['FullName']==chosen, ['RaceNumber', 'GridPosition', 'Position']]
filtered_df['GridPosition'] = filtered_df['GridPosition'].fillna(21)
filtered_df['Position'] = filtered_df['Position'].fillna(21)

filtered_df['PositionChanged'] = filtered_df['GridPosition'] - filtered_df['Position']

plt.bar(filtered_df['RaceNumber'], filtered_df['PositionChanged'], color = "red", width = 0.5)
plt.title(f"Difference between Start and Finish Position for {chosen}")
plt.xlabel("Race Number")
plt.ylabel("Position Difference")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()