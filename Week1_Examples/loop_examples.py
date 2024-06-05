# Loop examples

# Example 1:
#
# Get a number of lines from the user
# Print (line number + 1) stars on each line
#
# So, if the user enters 5, the output should be:
# **
# ***
# ****
# *****
# ******
#

# Get the number of lines from the user
#
# Important!!!! input() returns a string!!!!!!!!
numLines = int(input("Enter the number of lines: "))

# Loop over the lines
#
# The loop variable (which will be the line number),
# i, will go from 1 to numLines, inclusive
#
for i in range(1, numLines+1):
    # Print the stars
    #
    # The loop variable, j, will go from 0 to i, inclusive
    #
    #    i     j    Output
    #    1     0
    #          1    **
    #    2     0
    #          1
    #          2    ***
    #    3     0
    #          1
    #          2
    #          3    ****
    # etc.
    for j in range(i+1):
        print("*", end="") # Print a star without a newline
    print()  # Print a newline


# Example 2:

# loop through a specified list

names = ["John", "Paul", "George", "Ringo"]

for name in names:
    print(name)

# Example 3:

# loop through a specified list, with an index

names = ["John", "Paul", "George", "Ringo"]

# len(names) = 4
# range(4) = [0, 1, 2, 3]
# i will be 0, 1, 2, 3

for i in range(len(names)):
    print(i, names[i])

# Example 4:

mylist = [1, 3.14159, "Hello", True]

for i in mylist:
    print(i)

# Example 5:

age = 1

while age < 21:
    print("You are", age, "years old - no alcohol for you!")
    age = age + 1

print("You are", age, "years old - you can drink now!")

# Summary:
#
# 1.  The for loop is used to iterate over a sequence
# (e.g., a list, a string, a range of numbers).  The
# general format is:
#
# for loop_variable in Python_list_sequence:

# 2.  The while loop is used to execute a block of code
# as long as a condition is true.  The general format is:

# while condition:

# 'condition' is a boolean (i.e. True/False) expression that is evaluated
# before each iteration of the loop.  If the condition
# is true, the block of code is executed.  If the condition
# is false, the loop is exited and the program continues

my_list = ["John", "Paul", "George", "End", "Ringo"]

for item in my_list:
    if item == "End":
        break
    print(item)