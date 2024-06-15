matrixA = [] # 1 x N matrix
matrixB = [] # N x N matrix
matrixC = []
#reading the row of integers from the input and returning it as a list
def read_matrices():
    return list(map(int, input().split())) #reads matrix A and B
#input().split() splits the input into integers
def matrix_multiplication(matrixA, matrixB):
    row_A, col_A = len(matrixA), len(matrixA[0])
    row_B, col_B = len(matrixB), len(matrixB[0])
#checking if rows of matrix A are not equal to columns of matrix B
    #resulting in error message
    if col_A != row_B:
        print("The input matrices cannot be multiplied! Rows of A not equal to columns of B!")
        return None
#set elements of matrix C to 0
    #copilot used for this formula
    matrixC = [[0] * col_B for _ in range(row_A)]
#create 3 loop
    for i in range(row_A):
        for j in range(col_B):
            for k in range(col_A):
                matrixC[i][j] += matrixA[i][k] * matrixB[k][j]

    return matrixC

matrixA = [read_matrices()]

N = len(matrixA[0])
matrixB = [read_matrices() for _ in range(N)]
#print the results, which are the elements of matrix C
matrixC = matrix_multiplication(matrixA, matrixB)

if matrixC:
    for row in matrixC:
        print(*row)


