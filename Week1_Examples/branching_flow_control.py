import random

random_number = random.random()

print("Evaluating if-else ... ")
if random_number < 0.5:
    print("First part of if-else construct.")
else:
    print("Second part of if-else construct")

print()

print("Starting for loop ... ")
for i in range(10):
    print("Iteration number", i+1)

print("Ended for loop.")
print()

list_name = ["a", "b", "c", "d", "e"]
counter = 1
print("Starting second for loop ... ")
for item in list_name:
    print("Iteration number ", counter, ", list element = ", item)
    counter = counter + 1

print("Ended second for loop.")
print()

a = 0
loop_condition = True
print("Starting while loop ... ")
while loop_condition:
    print("Iteration number ", a+1)
    a = a + 1
    if a >= 9:
        loop_condition = False

print("Ended while loop.")
print()

random_list = []
for i in range(12):
    random_number = random.random()
    if random_number < 0.5:
        random_list.append("True")
    else:
        random_list.append("False")

print (random_list)
