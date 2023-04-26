import random

projectedWinPercentage = 0.85

currentGames = 2103
currentWins = 1331

currentPercentage = 1.0*currentWins/currentGames

while (currentPercentage < 0.65):
    randomNumber = random.random()
    if (randomNumber < projectedWinPercentage):
        currentWins += 1
    currentGames += 1
    currentPercentage = 1.0*currentWins/currentGames

print ("Total games = ",currentGames)
print ("Total wins = ", currentWins)
print ("Win percentage = ", currentPercentage)