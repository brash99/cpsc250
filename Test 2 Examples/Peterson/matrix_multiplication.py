matrixA = []
matrixB = []
matrixC = []


def matrix_multiplication():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    A = list(map(int, data[0].split()))
    N = len(A)
    B = []
    for i in range(1, N + 1):
        row = list(map(int, data[i].split()))
        B.append(row)
    if len(B) != N or any(len(row) != N for row in B):
        print("The input matrices cannot be multiplied! Rows of A not equal to columns of B!")
        return
    C = [0] * N
    for i in range(N):
        for j in range(N):
            C[i] += A[j] * B[j][i]

    print(' '.join(map(str, C)))

if __name__=="__main__":
    matrix_multiplication()

