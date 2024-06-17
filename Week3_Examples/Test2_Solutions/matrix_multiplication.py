matrixA = []
matrixB = []
matrixC = []

# Type your code here.
# Make a list for A from the integers on the first line
matrixA = [int(n) for n in input().split()]

size = len(matrixA)

# Multiply A x B
try:
    # Input matrix B by inputting a list from each line and
    # appending the list to matrix B
    for i in range(size):
        matrixB.append([int(n) for n in input().split()])
    
    for i in range(size):
        val = 0
        for j in range(size):
            val = val + (matrixA[j] * matrixB[j][i]);
        matrixC.append(val)
        
    # Output matrix C
    for n in matrixC:
        print(n, end = ' ')
    print()
except:
    print("The input matrices cannot be multiplied! Rows of A not equal to columns of B!")
