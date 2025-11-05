#Enter a driver's name and get their points per race and total number of points

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("/Users/maireadodwyer/Desktop/f1_winner_prediction/data/processed/f1_2025_results.csv")

driver_names = np.array(df['FullName'].unique())
print("Enter one of the following names: ")
for i in range(0,len(driver_names)):
    print(f"{driver_names[i]} \n")

chosen = input()

filtered_df = df.loc[df['FullName'] == chosen, ['RaceNumber', 'Points']]

print(filtered_df)

plot = filtered_df.plot(
    kind = 'line',
    x = 'RaceNumber',
    y = 'Points',
    color = 'blue',
    title = chosen,
    legend=False,
)

plot.set_xlabel("Race Number")
plot.set_ylabel("Points")
plt.xticks(np.arange(0, 21, 1))
plt.show()

filtered_df['CumulativePoints'] = np.cumsum(filtered_df['Points'])

plot2 = filtered_df.plot(
    kind = 'line',
    x = 'RaceNumber',
    y = 'CumulativePoints',
    color = 'green',
    title = chosen,
    legend = False,
)

plot2.set_xlabel("Race Number")
plot2.set_ylabel("Cumulated Points")
plt.xticks(np.arange(0, 21, 1))
plt.show()