def required_wins_to_percentage(current_games, current_wins, target_percentage, projected_percentage):
    current_percentage = current_wins / current_games

    if current_percentage >= target_percentage:
        return 0

    # The algorithm:
    #
    # We start with current_wins.  The additional wins will be required_games*projected_percentage
    # So, total_wins will be the sum of these two numbers.
    #
    # The total number of games will be current_games + required_games
    #
    # The target percentage will be the ratio of total_wins / total_games
    #
    # target_percentage = (current_wins + required_games*projected_percentage)/(current_games + required_games)
    #
    # Now, solve this for required_games!
    #
    # target_percentage*(current_games + required_games) = current_wins + required_games*projected_percentage
    # required_games*(target_percentage - projected_percentage) = current_wins - target_percentage*current_games
    # required_games = (current_games*target_percentage - current_wins)/(projected_percentage - target_percentage)

    required_games = (current_games * target_percentage - current_wins) / (projected_percentage - target_percentage)
    required_wins = required_games * projected_percentage

    return round(required_wins), round(required_games)


currentGames = 2103
currentWins = 1331
# currentGames = 2200
# currentWins = 1410

targetPercentage = 0.65
projectedPercentage = 0.80

requiredWins, requiredGames = required_wins_to_percentage(currentGames, currentWins,
                                                          targetPercentage, projectedPercentage)

print(f"You need {requiredWins} more wins, out of an additional {requiredGames} games, to "
      f"achieve a {targetPercentage*100}% win percentage in {currentGames+requiredGames} total games.")
