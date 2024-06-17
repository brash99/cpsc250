# Read a line of input of integers and store them in a matrix
matrixA = [int(x) for x in input().split()]

# get the number of elements in A
N = len(matrixA)

# read in a second matrix with N lines of integers
matrixB = []
for i in range(N):
    matrixB.append([int(x) for x in input().split()])

# create a matrix to store the result
matrixC = []

# multiply the two matrices
for i in range(N):
    matrixC.append([0]*N)
    for j in range(N):
        for k in range(N):
            matrixC[i][j] += matrixA[k] * matrixB[k][j]

# output the result
for i in range(N):
    print(matrixC[i], end=' ')
print()
