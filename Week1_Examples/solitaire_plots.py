import random
import math
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

numSims = 100000
projectedWinPercentage = 0.82
startGames = 2103
startWins = 1331
# startGames = 2230
# startWins = 1433
desiredPercentage = 0.65
chatgpt_prediction = 211
# chatgpt_prediction = 118

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

hbins = 200

fig, axs = plt.subplots(2, 2)
fig.tight_layout(pad=2.0)
axs[0][0].hist(gamesRequired, bins=hbins)
axs[0][0].title.set_text('Total Games Required')
axs[0][1].hist(gamesWon, bins=hbins)
axs[0][1].title.set_text('Total Games Won')
axs[1][0].hist(finalPercentage, bins=hbins)
axs[1][0].title.set_text('Overall Win Percentage')

axs[1][1].hist(latentPercentage, bins=hbins)
axs[1][1].title.set_text('Latent Win Percentage')

# Here is a simple (but wrong!) model of what the latentPercentage distribution
# should look like
std = 1.0/math.sqrt(chatgpt_prediction)/2.5
mu = 1.01*projectedWinPercentage

xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, hbins)
p = numSims/hbins/2.0*norm.pdf(x, mu, std)
axs[1][1].plot(x, p, 'k', linewidth=2)

plt.show()
