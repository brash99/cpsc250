import random

seed = 42
random.seed(seed)

number_of_randoms = 10

#for i in range(number_of_randoms):
#    r_num = random.randint(1, 6)
#    print(f"Random number {i+1}: {r_num}")

#for i in range(number_of_randoms):
#    r_num = 100.0 + random.random()*100.0
#    print(f"Random number {i+1}: {r_num}")

my_choices = ['rock', 'paper', 'scissors']

for i in range(number_of_randoms):
    r_choice = random.choice(my_choices)
    print(f"Random choice {i+1}: {r_choice}")
