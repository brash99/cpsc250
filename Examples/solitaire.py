import random
import numpy as np
import pandas as pd
import scipy as sc
import matplotlib.pyplot as plt

numSims = 10000
projectedWinPercentage = 0.82

gamesRequired = []

for i in range(numSims):

    currentGames = 2103
    currentWins = 1331

    currentPercentage = 1.0*currentWins/currentGames

    while currentPercentage < 0.65:
        randomNumber = random.random()
        if randomNumber < projectedWinPercentage:
            currentWins += 1
        currentGames += 1
        currentPercentage = 1.0*currentWins/currentGames

    gamesRequired.append(currentGames)

plt.hist(gamesRequired)
plt.show()
