import random
import math
import matplotlib.pyplot as plt

plot_choice = 3

x1 = []
y1 = []
x2 = []
y2 = []
dist = []
d1 = []
d2 = []
d3 = []

npts = 10000000
ng = 0
for i in range(npts):

    x1.append(random.random())
    y1.append(0.0)

    test = random.randint(1, 4)
    if test == 1:
        x2.append(random.random())
        y2.append(0.0)
        d1.append(math.sqrt((x2[i] - x1[i]) ** 2 + (y2[i] - y1[i]) ** 2))
    elif test == 2:
        x2.append(random.random())
        y2.append(1.0)
        d2.append(math.sqrt((x2[i] - x1[i]) ** 2 + (y2[i] - y1[i]) ** 2))
        d1.append(math.sqrt((x2[i] - x1[i]) ** 2 + (y2[i] - y1[i]) ** 2))
    elif test == 3:
        y2.append(random.random())
        x2.append(0.0)
        d3.append(math.sqrt((x2[i] - x1[i]) ** 2 + (y2[i] - y1[i]) ** 2))
        d2.append(math.sqrt((x2[i] - x1[i]) ** 2 + (y2[i] - y1[i]) ** 2))
        d1.append(math.sqrt((x2[i] - x1[i]) ** 2 + (y2[i] - y1[i]) ** 2))
    else:
        y2.append(random.random())
        x2.append(1.0)
        d3.append(math.sqrt((x2[i] - x1[i]) ** 2 + (y2[i] - y1[i]) ** 2))
        d2.append(math.sqrt((x2[i] - x1[i]) ** 2 + (y2[i] - y1[i]) ** 2))
        d1.append(math.sqrt((x2[i] - x1[i]) ** 2 + (y2[i] - y1[i]) ** 2))

    x_values = [x1[i], x2[i]]
    y_values = [y1[i], y2[i]]
    if plot_choice == 2:
        plt.plot(x_values, y_values, 'bo', linestyle="--")

    dist.append(math.sqrt((x2[i] - x1[i])**2 + (y2[i] - y1[i])**2))

    if dist[i] > 1:
        ng = ng + 1

print(f"Probability = {ng/npts*1.0:.5f}")
print(f"Theory: {3.0/4.0-math.pi/8.0:.5f}")
nbins = 50

if plot_choice == 1:
    plt.hist(dist, bins=nbins)
    plt.title("Simulation of Chords of a Square")
    plt.xlabel("Distance between Points")
    plt.ylabel("Frequency")
elif plot_choice == 3:
    plt.hist(d1, bins=nbins, label='Same Side')
    plt.hist(d2, bins=nbins, label='Opposite Sides')
    plt.hist(d3, bins=nbins, label='Adjacent Sides')
    plt.title("Simulation of Chords of a Square")
    plt.xlabel("Distance between Points")
    plt.ylabel("Frequency")

plt.legend()
plt.show()
