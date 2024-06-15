#Not quite sure how to write the input statement to take matricies

matrixA = []
matrixB = []
matrixC = []

import numpy as np
A = input('enter matrix a')
B = input('enter matrix b')
result = []
matrixA = np.array([A])
matrixB = np.array([B])

#I used a youtube tutorial for this part, I wanted to make sure I understood exactly how the for loop multiplied the values vs. using chat gpt
for i in range(len(matrixA)):
    for j in range(len(matrixB)):
        for k in range(len(matrixB)):
           result[i][j] += (matrixA[i][j] * matrixB[k][j])
for r in result:
    print(r)

