matrixA = []
matrixB = []
matrixC = []

# input for the matrix A
matrixA = list(map(int, input().split()))
x = len(matrixA)

# input for the matrix B
for _ in range(x):
    row = list(map(int, input().split()))
    matrixB.append(row)

# Check to see if we can multiply the matrices
if any(len(row) != x for row in matrixB):
    print("The input matrices cannot be multiplied! Rows of A not equal to columns of B!")
else:
    # multiply the matrices
    for j in range(x):
        result = 0
        for k in range(x):
            result += matrixA[k] * matrixB[k][j]
        matrixC.append(result)

    # Print the matrix
    for value in matrixC:
        print(value, end=' ')
