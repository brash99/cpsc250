import random
import numpy as np
import matplotlib.pyplot as plt

numSims = 10000
projectedWinPercentage = 0.80
startGames = 2103
startWins = 1331

desiredPercentage = 0.65
chatgpt_prediction = 240

gamesRequired = []
gamesWon = []
finalPercentage = []
latentPercentage = []

for i in range(numSims):

    currentGames = startGames
    currentWins = startWins

    currentPercentage = 1.0*currentWins/currentGames

    while currentPercentage < desiredPercentage:
        randomNumber = random.random()
        if randomNumber < projectedWinPercentage:
            currentWins += 1
        currentGames += 1
        currentPercentage = 1.0*currentWins/currentGames

    gamesRequired.append(currentGames)
    gamesWon.append(currentWins)
    finalPercentage.append(currentWins/currentGames)
    latentPercentage.append((currentWins-startWins)/(currentGames-startGames))

fig, axs = plt.subplots(2, 2)
fig.tight_layout(pad=2.0)

axs[0][0].plot(gamesRequired, gamesWon, '.')
axs[0][0].title.set_text('Games Won vs. Games Required')

axs[0][1].plot(gamesRequired, gamesWon, '.')
axs[0][1].title.set_text('First Plot Expanded')
x_low = 2337
x_high = 2350
y_low = 1519
y_high = 1528
axs[0][1].set_xlim([x_low, x_high])
axs[0][1].set_ylim([y_low, y_high])
axs[0][1].set_xticks(np.arange(x_low, x_high, 1))
axs[0][1].set_yticks(np.arange(y_low, y_high, 1))
axs[0][1].tick_params(axis='x', rotation=90)
axs[0][1].xaxis.grid(color='gray', linestyle='dashed')
axs[0][1].yaxis.grid(color='gray', linestyle='dashed')


xpath1 = [2338, 2339, 2340]
ypath1 = [1519, 1520, 1521]
axs[1][0].plot(xpath1, ypath1, 'r.-')
xpath2 = [2340, 2341, 2342, 2343]
ypath2 = [1520, 1521, 1522, 1523]
axs[1][0].plot(xpath2, ypath2, 'g.-')
xpath3 = [2343, 2344, 2345, 2346]
ypath3 = [1522, 1523, 1524, 1525]
axs[1][0].plot(xpath3, ypath3, 'm.-')
xpath4 = [2346, 2347, 2348, 2349]
ypath4 = [1524, 1525, 1526, 1527]
axs[1][0].plot(xpath4, ypath4, 'c.-')
axs[1][0].plot(gamesRequired, gamesWon, 'b.')

axs[1][0].title.set_text('Paths to Victory')
axs[1][0].set_xlim([x_low, x_high])
axs[1][0].set_ylim([y_low, y_high])
axs[1][0].set_xticks(np.arange(x_low, x_high, 1))
axs[1][0].set_yticks(np.arange(y_low, y_high, 1))
axs[1][0].tick_params(axis='x', rotation=90)
axs[1][0].xaxis.grid(color='gray', linestyle='dashed')
axs[1][0].yaxis.grid(color='gray', linestyle='dashed')

x4 = [x_low+i for i in range(x_high-x_low+1)]
y4 = [0.65*x4[i] for i in range(x_high-x_low+1)]
axs[1][0].plot(x4,y4,'y--')

x_low = 2314
x_high = 2350
y_low = 1500
y_high = 1528

#xpath1 = [2338, 2339, 2340]
#ypath1 = [1519, 1520, 1521]
#axs[1][1].plot(xpath1, ypath1, 'y.-')

xpath2 = [i for i in range(x_low+1,2344)]
ypath2 = [1501,1502,1503,1504,1505,1505,1506,1507,1508,1509,1509,
          1510,1510,1511,1512,1513,1514,1514,1515,1515,1516,1517,
          1518,1519,1519,1520,1521,1522,1523]
axs[1][1].plot(xpath2, ypath2, 'g.-')

#xpath3 = [2343, 2344, 2345, 2346]
#ypath3 = [1522, 1523, 1524, 1525]
#axs[1][1].plot(xpath3, ypath3, 'y.-')
#xpath4 = [2346, 2347, 2348, 2349]
#ypath4 = [1524, 1525, 1526, 1527]
#axs[1][1].plot(xpath4, ypath4, 'y.-')
axs[1][1].plot(gamesRequired, gamesWon, 'b.')

#axs[1][1].title.set_text('Paths to Victory')
axs[1][1].set_xlim([x_low, x_high])
axs[1][1].set_ylim([y_low, y_high])
axs[1][1].set_xticks(np.arange(x_low, x_high, 3))
axs[1][1].set_yticks(np.arange(y_low, y_high, 3))
axs[1][1].tick_params(axis='x', rotation=90)
axs[1][1].xaxis.grid(color='gray', linestyle='dashed')
axs[1][1].yaxis.grid(color='gray', linestyle='dashed')

plt.show()
