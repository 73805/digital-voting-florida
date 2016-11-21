import matplotlib.pyplot as plt
import pandas as pd

florida = pd.read_csv("florida_clean.csv", header=0)
wisconsin = pd.read_csv("wisconsin_clean.csv", header=0)

x_florida = florida["dem"].tolist()
x_florida = [int(i) for i in x_florida]
y_florida = florida["rep"].tolist()
y_florida = [int(i) for i in y_florida]
florida_colors = florida["digital"].tolist()


for i in range(0, len(florida_colors)):
    if florida_colors[i] == 1:
        florida_colors[i] = "orange"
    else:
        florida_colors[i] = "green"
        
x_wisconsin = wisconsin["dem"].tolist()
x_wisconsin = [int(i) for i in x_wisconsin]
y_wisconsin = wisconsin["rep"].tolist()
y_wisconsin = [int(i) for i in y_wisconsin]
wisconsin_colors = wisconsin["digital"].tolist()


for i in range(0, len(wisconsin_colors)):
    if wisconsin_colors[i] == 1:
        wisconsin_colors[i] = "orange"
    else:
        wisconsin_colors[i] = "green"

plt.clf()
plt.figure(1)
plt.scatter(x_florida, y_florida, s=60, c=florida_colors)
plt.grid(True, which='both')
plt.xlabel("Democrat Vote Change")
plt.ylabel("Republican Vote Change")
plt.title('Florida County Voting Shifts')
plt.annotate("Orange -> Digital Voting Available", (30000, 41000))

plt.figure(2)
plt.scatter(x_wisconsin, y_wisconsin, s=60, c=wisconsin_colors)
plt.grid(True, which='both')
plt.xlabel("Democrat Vote Change")
plt.ylabel("Republican Vote Change")
plt.title('Wisconsin County Voting Shifts')
plt.annotate("Orange -> Digital Voting Available", (30000, 41000))
plt.xlim(-9000, 1000)
plt.ylim(-5000, 5000)
