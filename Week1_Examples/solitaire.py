import random
import matplotlib.pyplot as plt

# Initial parameters
numSims = 10000  # how many times we will "simulate" the game playing.
projectedWinPercentage = 0.80  # win percentage to be used going forward
startGames = 2103
startWins = 1331
# startGames = 2200  # total number of games played thus far
# startWins = 1410  # total number of wins thus far
desiredPercentage = 0.65  # target win percentage
chatgpt_prediction = 211
# chatgpt_prediction = 118  # what ChatGPT solution estimated for the required number of games

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
plt.hist(gamesRequired, bins=h_bins)
plt.show()
