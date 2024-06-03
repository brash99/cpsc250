# Loop examples

# Example 1:
#
# Get a number of lines from the user
# Print (line number + 1) stars on each line
#

# Get the number of lines from the user
numLines = int(input("Enter the number of lines: "))

# Loop over the lines
#
# The loop variable, i, will go from 1 to numLines, inclusive
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
    print() # Print a newline