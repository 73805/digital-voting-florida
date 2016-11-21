import matplotlib.pyplot as plt
import pandas as pd

# getting the input CSV
florida = pd.read_csv("clean_florida.csv", header=0)

x = florida["dem"].tolist()
x = [int(i) for i in x]
y = florida["rep"].tolist()
y = [int(i) for i in y]

colors = florida["digital"].tolist()

for i in range(0, len(colors)):
    if colors[i] == 1:
        colors[i] = "orange"
    else:
        colors[i] = "green"

plt.clf()
plt.scatter(x, y, s=60, c=colors)
plt.grid(True, which='both')
plt.xlabel("Democrat Vote Change")
plt.ylabel("Republican Vote Change")
plt.title('Florida County Voting Shifts')
plt.annotate("Orange -> Digital Voting Available", (30000, 41000))
