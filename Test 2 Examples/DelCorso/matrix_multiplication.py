matrixA = []
matrixB = []
matrixC = []

# Type your code here
def getting_the_input():
   # user inputs the data on their own.
   matrixA = [list(map(int, input().split()))]

   matrixB = []
   for mBA in range(len(matrixA[0])):
       matrixB.append(list(map(int, input().split())))
   return matrixA, matrixB
def matrix_times(a, b):
   if len(a[0]) != len(b):
       return "The input matrices cannot be muliplied! Rows of A not equal to columns of B!"
   # Initialize the result matrix with inside for loop.
   c = [[0 for mBA in range(len(b[0]))] for mBA in range(len(a))]

   # Perform the matrix multiplication
   for i in range(len(a)):
       for j in range(len(b[0])):
           for k in range(len(b)):
               c[i][j] += a[i][k] *b[k][j]
   return c

if __name__ == '__main__':
   matrixA, matrixB = getting_the_input()
   matrixC = matrix_times(matrixA, matrixB)
   if isinstance(matrixC, str):
       print(matrixC)
   else:
       print(matrixC)