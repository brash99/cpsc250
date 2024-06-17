matrixA = []
matrixB = []
matrixC = []
# REMEMBER TO COMMENT
# Type your code here

# read input
data = input().strip().split('\n')
print(data)

# read first line,(suggested code from pycharm)
matrixA = list(map(int, data[0].strip().split()))
N= len(matrixA)

print(matrixA)
print(N)

# read next lines for Maxtrix b

if len(data) - 1 != N:
    print('The input matrices cannot be multiplied! Rows of A not equal to columns of B!')
else:
    for i in range(1, N+1):
        row = list(map(int, data[i].strip().split()))
        if len(row) != N:
            print('The input matrices cannot be multiplied! Rows of A not equal to columns of B!')
            break
        matrixB.append(row)

# start matrix c with zeros
matrixC = [0] * N

#multiplu a and b together to get C (code slightly filled in by pycharm)
for j in range(N):
    for k in range(N):
        matrixC[j] += matrixA[k] * matrixB[k][j]


# print result matrix
print(' '.join(map(str, matrixC)))
