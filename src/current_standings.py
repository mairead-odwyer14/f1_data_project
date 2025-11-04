import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("/Users/maireadodwyer/Desktop/f1_winner_prediction/data/processed/f1_2025_results.csv")

df.sort_values(df.columns[2],
               axis = 0,
               inplace = True)

driver_standings = (
    df.groupby("FullName", as_index=False)["Points"]
    .sum()
    .sort_values("Points", ascending=False)
)

ax = driver_standings.plot(kind = 'bar',
                    x = 'FullName',
                    y = 'Points',
                    color='blue',
                    title='Current Standings',
                    legend=False
)

ax.set_xlabel("Driver")
ax.set_ylabel("Points")

team_standings = (
    df.groupby("TeamName", as_index=False)["Points"]
    .sum()
    .sort_values("Points", ascending=True)
)

bx = team_standings.plot(kind = 'bar',
                                x = 'TeamName',
                                y = 'Points',
                                color = 'red',
                                title = 'Points per Team',
                                legend=False
)

bx.set_xlabel("Team")
bx.set_ylabel("Points")
plt.show()
