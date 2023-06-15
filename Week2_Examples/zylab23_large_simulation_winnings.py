# Step 0:  Provided code.  Imports random library, and GVDie class definition.  Gets a random
#          number seed from the user.  Gets the number of "lives" from the user for the game.

import random
import gv_die
import matplotlib.pyplot as plt

# Read random seed to support testing (do not alter) and starting credits
seed = int(input())
# Set the seed for random
random.seed(int(seed))

# Initial credits
initial_credits = int(input())

# Step 1a:   (i) Define two new GVDie objects, and define initial values for the number of rounds
#               played, and goal to be reached for the next roll.
#           (ii) begin main game loop (while lives still left)

die1 = gv_die.GVDie()
die2 = gv_die.GVDie()

num_sims = 300
round_result = []
credit_result = []
result_number = []

factors = [1.01, 1.02, 1.03, 1.05, 1.07, 1.1, 1.2, 1.3, 1.4, 1.5, 1.75, 2.0, 2.5, 3.0, 4.0, 5.0]
tw = []

for f in range(len(factors)):

    # stop playing if the player is "up" by the chosen factor
    stop_playing_ahead = factors[f]*initial_credits
    print("Positive Limit: ",stop_playing_ahead)

    # stop playing if the player is "down" by the chosen factor
    # stop_playing_behind = 0
    # stop_playing_behind = 50.0
    stop_playing_behind = initial_credits/factors[f]
    print("Negative Limit: ", stop_playing_behind)

    total_winnings = 0.0

    for i in range(num_sims):

        total_winnings -= initial_credits

        credit_round = []
        result_round = []
        result_count = 0

        credits = initial_credits
        goal = -1
        rounds = 0

        quit = False

        while credits > 0 and not quit:
            rounds += 1

            # Step 1b:  (i) Roll both dice, get total, and print total.
            #           (ii) Player wins one credit by rolling 7 or 11
            #           (iii) Player loses one credit by rolling 2, 3 or 12
            #           (iv) Otherwise, set the goal for the next round and continue on
            die1.roll()
            die2.roll()
            total = die1.get_value() + die2.get_value()
            # print(f'Dice total: { total }')

            if total == 7 or total == 11:
                credits += 1
                credit_round.append(credits)
                result_count += 1
                result_round.append(result_count)
                if credits >= stop_playing_ahead:
                    total_winnings += credits
                    quit = True
            elif total <= 3 or total == 12:
                credits -= 1
                credit_round.append(credits)
                result_count += 1
                result_round.append(result_count)
                if credits <= stop_playing_behind:
                    total_winnings += credits
                    quit = True
            else:
                goal = total

            # Step 2: Continue rolling until player wins or loses
            while goal != -1:
                die1.roll()
                die2.roll()
                total = die1.get_value() + die2.get_value()
                # print(f'Dice total: {total}')

                # Player loses one credit
                if total == 7:
                    credits -= 1
                    goal = -1
                    credit_round.append(credits)
                    result_count += 1
                    result_round.append(result_count)
                    if credits <= stop_playing_behind:
                        total_winnings += credits
                        quit = True
                # Player wins one credit
                elif total == goal:
                    credits += 1
                    goal = -1
                    credit_round.append(credits)
                    result_count += 1
                    result_round.append(result_count)
                    if credits >= stop_playing_ahead:
                        total_winnings += credits
                        quit = True

            # print(f'Credits: {credits}')

        # print(f'Rounds: { rounds }')
        round_result.append(rounds)
        credit_result.append(credit_round)
        result_number.append(result_round)

    print(f'Total Winnings: { total_winnings }')
    tw.append(total_winnings)

    print(factors, tw)

plt.plot(factors, tw, 'r-o')
plt.title("Lucky7 Simulations:  Total Winnings for Various Stopping Points")
plt.xlabel("Stopping Factor")
plt.ylabel("Total Winnings")
plt.show()
