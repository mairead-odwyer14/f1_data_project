import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("/Users/maireadodwyer/Desktop/f1_winner_prediction/data/processed/f1_2025_results.csv")

df.sort_values(df.columns[2],
               axis = 0,
               inplace = True)

standings = (
    df.groupby("FullName", as_index=False)["Points"]
    .sum()
    .rename(columns={"Points": "points"})
    .sort_values("points", ascending=False)
)

ax = standings.plot(kind = 'bar',
                    x = 'FullName',
                    y = 'points',
                    color='blue',
                    title='Current Standings',
                    legend=False
)

ax.set_xlabel("Driver")
ax.set_ylabel("Points")
plt.show()

print(standings.to_string(index=False))