matrixA = []
matrixB = []
matrixC = []

# Type your code here
matrixA = [int(i) for i in input().split()] #input matrixA list of integers
N = len(matrixA) #calculating N value
matrixB = [] #list of N integers
for i in range(N):
    matrixB.append([int(i) for i in input().split()])
matrixC = [0 for i in range(N)]
for i in range(N):
    for j in range(N):
        matrixC[i] = matrixC[i] + matrixA[j] * matrixB[j][i] #calculate the matrix multiplication
print(matrixC) #output for matrixC

