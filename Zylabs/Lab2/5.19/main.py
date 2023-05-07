user_values = []

# Input begins with an integer indicating the number of integers that follow
num_values = int(input())

# Get list of integers from input
for i in range(num_values):
    user_input = float(input())
    user_values.append(user_input)

# Find the minimum value
max_value = max(user_values)

# Divide while outputting
for i in range(num_values): 
    print(f'{user_values[i] / max_value:.2f}')
