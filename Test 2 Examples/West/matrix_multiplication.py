#get inputs for matrix a, i used chat gpt to help me make this efficient line
matrixA = list(map(int, input().split()))
matrixB = []
matrixC = []


#create variable n to use in the rest of the code
n = len(matrixA)

#append inputs to matrixB to make it and also check to see if rows of a match colums of b
# I also used chat gpt to help me get the input
for i in range(n):
    row = list(map(int, input().split()))
    if len(row) != n:
        print('The input matrices cannot be multiplied! Rows of A not equal to columns of B!')
    matrixB.append(row)

# multiplying the two matricies together by ahving a sum variable that gets updated and appended to matrix c
for i in range(n):
    sum = 0
    for j in range(n):
        sum += matrixA[j] * matrixB[j][i]
    matrixC.append(sum)
#finally formatting the answer, I used chat gpt to help me make this easy line of code
print(" ".join(map(str, matrixC)))