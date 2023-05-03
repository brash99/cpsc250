def required_wins_to_percentage(total_games, total_wins, target_percentage):
    current_percentage = total_wins / total_games

    if current_percentage >= target_percentage:
        return 0

    required_games = (total_games * target_percentage - total_wins) / (target_percentage - current_percentage)
    required_wins = required_games * target_percentage

    return round(required_wins - total_wins)


totalGames = 100
totalWins = 25
targetPercentage = 0.70

requiredWins = required_wins_to_percentage(totalGames, totalWins, targetPercentage)

print(f"You need {requiredWins} more wins to achieve a "
      f"{targetPercentage*100}% win percentage in {totalGames} games.")
