import random
import matplotlib.pyplot as plt

currentGames = 2103
currentWins = 1331

currentPercentage = 1.0*currentWins/currentGames
projectedWinPercentage = 0.85

numSims = 100
gamesRequired = []

while (currentPercentage < 0.65):
    randomNumber = random.random()
    if (randomNumber < projectedWinPercentage):
        currentWins +=1
    currentGames += 1
    currentPercentage = 1.0*currentWins/currentGames

gamesRequired.append(currentGames)

#print ("Total Games = ",currentGames)
#print ("Total Wins = ",currentWins)
#print ("Win Percentage = ",currentPercentage)