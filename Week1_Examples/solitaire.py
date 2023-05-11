import random
import math
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# Initial parameters
numSims = 10000  # how many times we will "simulate" the game playing.
projectedWinPercentage = 0.82  # win percentage to be used going forward
# startGames = 2103
# startWins = 1331
startGames = 2200  # total number of games played thus far
startWins = 1410  # total number of wins thus far
desiredPercentage = 0.65  # target win percentage
# chatgpt_prediction = 211
chatgpt_prediction = 118  # what ChatGPT solution estimated for the required number of games

# Create some empty lists to store values for each simulation
gamesRequired = []
gamesWon = []
finalPercentage = []
latentPercentage = []

# Main loop
for i in range(numSims):

    # Set initial values
    currentGames = startGames
    currentWins = startWins

    # Initialize current win percentage each time through the loop
    currentPercentage = 1.0*currentWins/currentGames

    # Keep playing games until we reach the desired win percentage
    while currentPercentage < desiredPercentage:
        # Pick a random number between 0 and 1
        randomNumber = random.random()
        # if random number is less than our stable win percentage, then we win this game!
        if randomNumber < projectedWinPercentage:
            currentWins += 1
        # update current number of games played
        currentGames += 1
        # update current win percentage
        currentPercentage = 1.0*currentWins/currentGames

    # Fill lists with results for this iteration through the loop
    gamesRequired.append(currentGames)
    gamesWon.append(currentWins)
    finalPercentage.append(currentWins/currentGames)
    latentPercentage.append((currentWins-startWins)/(currentGames-startGames))

# Number of bins in the histograms
h_bins = 200

# Create a 2 x 2 figure
fig, axs = plt.subplots(2, 2)
# Add some padding around each subplot, so that title does not overlap with axis labels
fig.tight_layout(pad=2.0)

# Draw the histograms, with appropriate titles
axs[0][0].hist(gamesRequired, bins=h_bins)
axs[0][0].title.set_text('Total Games Required')
axs[0][1].hist(gamesWon, bins=h_bins)
axs[0][1].title.set_text('Total Games Won')
axs[1][0].hist(finalPercentage, bins=h_bins)
axs[1][0].title.set_text('Overall Win Percentage')
axs[1][1].hist(latentPercentage, bins=h_bins)
axs[1][1].title.set_text('Latent Win Percentage')

# Here is a simple (but wrong!) model of what the latentPercentage distribution
# should look like
std = 1.0/math.sqrt(chatgpt_prediction)/2.5
mu = projectedWinPercentage

x_min, x_max = plt.xlim()
x = np.linspace(x_min, x_max, h_bins)
p = numSims/h_bins/2.5*norm.pdf(x, mu, std)
axs[1][1].plot(x, p, 'k', linewidth=2)

plt.show()
