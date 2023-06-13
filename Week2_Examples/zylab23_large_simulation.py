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

num_sims = 1000
round_result = []
credit_result = []
result_number = []

for i in range(num_sims):

    credit_round = []
    result_round = []
    result_count = 0

    credits = initial_credits
    goal = -1
    rounds = 0

    while credits > 0:
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

        elif total <= 3 or total == 12:
            credits -= 1
            credit_round.append(credits)
            result_count += 1
            result_round.append(result_count)
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
            # Player wins one credit
            elif total == goal:
                credits += 1
                goal = -1
                credit_round.append(credits)
                result_count += 1
                result_round.append(result_count)

        # print(f'Credits: {credits}')

    # print(f'Rounds: { rounds }')
    round_result.append(rounds)
    credit_result.append(credit_round)
    result_number.append(result_round)

hbins = 100
# plt.hist(round_result, hbins)
# plt.yscale('log')

# print(len(result_number))
# print(result_number)
# print(credit_result)

for j in range(len(result_number)):
    if len(result_number[j]) > 3000:
        plt.plot(result_number[j], credit_result[j])

plt.show()
