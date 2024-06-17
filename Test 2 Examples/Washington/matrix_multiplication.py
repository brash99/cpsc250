from typing import List


def matrix_multiply(A, B):
    # A is represented as a list of the integers found on the first line of input.
    # B is represented as a list of N rows
    N = len(B)
    C: list[int] = [0] * N

    # matrix multiplication
    for j in range(N):
        for i in range(N):
            C[j] += A[i] * B[i][j]

    return C


# Read input for matrix A
A = list(map(int, input().split()))

# Read input for matrix B
N = len(A)
B = []
for _ in range(N):
    row = list(map(int, input().split()))
    B.append(row)

# Calculate matrix product
C = matrix_multiply(A, B)

# Output the result
print(C)


# help from ChatGPT
