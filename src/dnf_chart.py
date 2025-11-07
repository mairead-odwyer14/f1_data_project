#Program to compute dnf count per team and display in a piechart
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df = pd.read_csv("/Users/maireadodwyer/Desktop/f1_winner_prediction/data/processed/f1_2025_results.csv")

teams_count = df.groupby("TeamName", as_index=False)["Status"].apply(lambda x: (x!='Finished').sum()).reset_index(names='count')


team_colours = {
    "Ferrari": "#F4320B",
    "Racing Bulls": "#3171FC",
    "Red Bull Racing": "#193CB8",
    "Aston Martin": "#0B3D2B",
    "Kick Sauber":  "#31C950",
    "Alpine": "#FC8DCA",
    "Williams": "#155DFC",
    "McLaren": "#FF8904",
    "Haas F1 Team": "#E7180B",
    "Mercedes": "#D6D3D1"
}

colors = [team_colours.get(team, "#CCCCCC") for team in teams_count["TeamName"]]

plt.figure(figsize=(10,10))
plt.pie(
    teams_count["count"],
    labels=teams_count["TeamName"],
    startangle=90,
    colors=colors
)

plt.title("Number of DNFs (Retired, DSQ, Lapped) per Team in F1 2025 Season")
plt.axis('equal')
plt.show()