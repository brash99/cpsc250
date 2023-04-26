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

current_games = 2103
current_wins = 1331
target_percentage = 0.65
projected_percentage = 0.82

required_wins, required_games = required_wins_to_percentage(current_games, current_wins, target_percentage, projected_percentage)

print(f"You need {required_wins} more wins, out of an additional {required_games} games, to achieve a {target_percentage*100}% win percentage in {current_games+required_games} total games.")
