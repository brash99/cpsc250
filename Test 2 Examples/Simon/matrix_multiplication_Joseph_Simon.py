matrixA = []
matrixB = []

# This should do the weird matrix multiplication.
def matrix_multiplyer(A,B):
    MatrixC = []  # Define MatrixC within the function
    for j in range(len(B[0])):  # Fix the range of the loop
        total = 0
        for i in range(len(A)):  # Fix the loop variable
            total += A[i] * B[i][j]
        MatrixC.append(total)
    return MatrixC

def main():
    matrixA.extend(map(int, input().split()))

    N = len(matrixA)
    for _ in range(N):
        row = list(map(int, input().split()))
        matrixB.append(row)

    if len(matrixA) != len(matrixB):
        print("The input matrices cannot be multiplied! Rows of A not equal to columns of B!")
        return

    matrixC = matrix_multiplyer(matrixA, matrixB)

    print(*matrixC)

if __name__ == "__main__":
    main()
