matrixA = []
matrixB = []
matrixC = []

def matrix_multiplication(matrixA, matrixB):
    N = len(matrixB)
    if len(matrixA) != N:
        return "The input matrices cannot be multiplied! Rows of A not equal to columns of B!"

    matrixC = [0] * N

    for i in range(N):
        for j in range(N):
            matrixC[i] += matrixA[j] * matrixB[j][i]

    return matrixC

if __name__ == "__main__":
    #Chatgpt was used during this portion
    import sys

    # Read all input lines from stdin
    input_data = sys.stdin.read().strip().split('\n')

    # Read matrix A (first line)
    matrixA = list(map(int, input_data[0].split()))

    # Determine size N from matrix B (number of rows)
    N = len(input_data) - 1

    # Read matrix B (next N lines)
    matrixB = []
    for i in range(1, N + 1):
        row = list(map(int, input_data[i].split()))
        matrixB.append(row)

    # Perform matrix multiplication
    matrixC = matrix_multiplication(matrixA, matrixB)

    # Print the result
    if isinstance(matrixC, str):
        print(matrixC)  # Print error message
    else:
        print(' '.join(map(str, matrixC)))