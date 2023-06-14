def print_list(mylist):
    for item in mylist:
        print(f'{item}', end=' ')
    print()


# Get a list of numbers from user
user_input = input()
user_list = user_input.split()
int_list = [int(element) for element in user_list]

# The goal is to remove all but the negative numbers from the list
# and print out this final list in order, in ascending order
#
# Example: if the original input is 12 10 -4 2 -3 -5 6 -7
# then the final output should be -3 -4 -5 -7

# Method 1:  With a for loop
negative_list1 = []

for element in int_list:
    if element < 0:
        negative_list1.append(element)

negative_list1.sort(reverse=True)
print_list(negative_list1)

# Method 2:  With list comprehension
negative_list2 = [element for element in int_list if element < 0]
negative_list2.sort(reverse=True)
print_list(negative_list2)

# Method 3: With lambda and filter()
negative_list3 = list(filter(lambda x: x < 0, int_list))
negative_list3.sort(reverse=True)
print_list(negative_list3)
