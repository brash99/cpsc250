

n = [1,19,165,289,149,55]

print("Number of games played: ", sum(n))

sum1 = 0
for i in range(len(n)):
    sum1 += (i+1)*n[i]

# print the expected value to three decimal places
print(f"Expected value of X is: {sum1/sum(n):.3f}")

# assume that going forward every 10 games results in [0,0,2,7,1,0]

current_average = sum1/sum(n)

while True:
    n_new = [0,0,2,7,1,0]
    for i in range(len(n)):
        n[i] += n_new[i]
    sum1 = 0
    for i in range(len(n)):
        sum1 += (i+1)*n[i]

    new_average = sum1/sum(n)
    #print(f"Expected value of X after {sum(n)} games is: {new_average:.3f}")

    if new_average <= 4.0:
        break

    current_average = new_average

print(f"Expected value of X after {sum(n)} games is: {new_average:.3f}")
