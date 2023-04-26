def required_wins_to_percentage(total_games, total_wins, target_percentage):
    current_percentage = total_wins / total_games

    if current_percentage >= target_percentage:
        return 0

    required_games = (total_games * target_percentage - total_wins) / (target_percentage - current_percentage)
    required_wins = required_games * target_percentage

    return round(required_wins - total_wins)

total_games = 100
total_wins = 25
target_percentage = 0.70

required_wins = required_wins_to_percentage(total_games, total_wins, target_percentage)

print(f"You need {required_wins} more wins to achieve a {target_percentage*100}% win percentage in {total_games} games.")
