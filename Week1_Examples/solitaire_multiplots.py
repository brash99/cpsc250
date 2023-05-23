import random
import numpy as np
import matplotlib.pyplot as plt

numSims = 10000
projectedWinPercentage = 0.82
# startGames = 2103
# startWins = 1331
startGames = 2200
startWins = 1410
desiredPercentage = 0.65
# chatgpt_prediction = 211
chatgpt_prediction = 118

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
x_low = 2297
x_high = 2307
y_low = 1493
y_high = 1500
axs[0][1].set_xlim([x_low, x_high])
axs[0][1].set_ylim([y_low, y_high])
axs[0][1].set_xticks(np.arange(x_low, x_high, 1))
axs[0][1].set_yticks(np.arange(y_low, y_high, 1))
axs[0][1].tick_params(axis='x', rotation=90)
axs[0][1].xaxis.grid(color='gray', linestyle='dashed')
axs[0][1].yaxis.grid(color='gray', linestyle='dashed')


xpath1 = [2298, 2299, 2300]
ypath1 = [1493, 1494, 1495]
axs[1][0].plot(xpath1, ypath1, 'r.-')
xpath2 = [2300, 2301, 2302, 2303]
ypath2 = [1494, 1495, 1496, 1497]
axs[1][0].plot(xpath2, ypath2, 'g.-')
xpath3 = [2303, 2304, 2305, 2306]
ypath3 = [1496, 1497, 1498, 1499]
axs[1][0].plot(xpath3, ypath3, 'm.-')
axs[1][0].plot(gamesRequired, gamesWon, 'b.')

axs[1][0].title.set_text('Paths to Victory')
axs[1][0].set_xlim([x_low, x_high])
axs[1][0].set_ylim([y_low, y_high])
axs[1][0].set_xticks(np.arange(x_low, x_high, 1))
axs[1][0].set_yticks(np.arange(y_low, y_high, 1))
axs[1][0].tick_params(axis='x', rotation=90)
axs[1][0].xaxis.grid(color='gray', linestyle='dashed')
axs[1][0].yaxis.grid(color='gray', linestyle='dashed')

xpath1 = [2298, 2299, 2300]
ypath1 = [1493, 1494, 1495]
axs[1][1].plot(xpath1, ypath1, 'r.-')
xpath2 = [2300, 2301, 2302, 2303]
ypath2 = [1494, 1495, 1496, 1497]
axs[1][1].plot(xpath2, ypath2, 'g.-')
xpath3 = [2303, 2304, 2305, 2306]
ypath3 = [1496, 1497, 1498, 1499]
axs[1][1].plot(xpath3, ypath3, 'm.-')
axs[1][1].plot(gamesRequired, gamesWon, 'b.')

x4 = [2297+i for i in range(10)]
y4 = [0.65*x4[i] for i in range(10)]
axs[1][1].plot(x4,y4,'c--')

axs[1][1].title.set_text('Paths to Victory')
axs[1][1].set_xlim([x_low, x_high])
axs[1][1].set_ylim([y_low, y_high])
axs[1][1].set_xticks(np.arange(x_low, x_high, 1))
axs[1][1].set_yticks(np.arange(y_low, y_high, 1))
axs[1][1].tick_params(axis='x', rotation=90)
axs[1][1].xaxis.grid(color='gray', linestyle='dashed')
axs[1][1].yaxis.grid(color='gray', linestyle='dashed')

plt.show()
