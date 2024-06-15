matrixA = []
matrixB = []
matrixC = []
def read_input():
    import sys
    input_data = sys.stdin.read().strip().split('\n')

    # Extracting matrixA dimensions
    dimensions = list(map(int, input_data.pop(0).split()))

    # Checking if dimensions match
    if dimensions[1] != len(input_data):
        print("The input matrices cannot be multiplied! Rows of A not equal to columns of B!")
        return None, None

    matrixA = [list(map(int, row.split())) for row in input_data]
    return matrixA, dimensions[0], dimensions[1]


def multiply_matrices(matrixA, matrixB, colsB):
    rowsA = len(matrixA)
    result = [[0] * colsB for _ in range(rowsA)]

    for i in range(rowsA):
        for j in range(colsB):
            for k in range(len(matrixB)):
                result[i][j] += matrixA[i][k] * matrixB[k][j]

    return result


def main():
    matrixA, rowsA, colsA = read_input()
    if matrixA is None:
        return

    matrixB = [list(map(int, input().split())) for _ in range(colsA)]

    if len(matrixB) != colsA:
        print("The input matrices cannot be multiplied! Rows of A not equal to columns of B!")
        return

    matrixC = multiply_matrices(matrixA, matrixB, colsA)
    for row in matrixC:
        print(' '.join(map(str, row)))


if __name__ == "__main__":
    main()
