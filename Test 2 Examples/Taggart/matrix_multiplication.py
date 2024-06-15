def matrix_multiplication(matrixA, matrixB):
    if len(matrixA) != len(matrixB[0]):
        return None, "The input matrices cannot be multiplied! Rows of A not equal to columns of B!"
    matrixC = []
    for i in range(len(matrixB[0])):
        row = 0
        for j in range(len(matrixA)):
            row += matrixA[j] * matrixB[j][i]
        matrixC.append(row)
    return matrixC, None

def main():
    matrixA = list(map(int, input().split()))
    N = len(matrixA)
    matrixB = [list(map(int, input().split())) for _ in range(N)]
    result, error = matrix_multiplication(matrixA, matrixB)
    if error:
        print(error)
    else:
        print(*result)
if __name__ == "__main__":
    main()