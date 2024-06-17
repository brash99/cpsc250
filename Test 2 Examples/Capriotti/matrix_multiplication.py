"""Takes a 1 x N matrix and an N x N matrix, multiplies them, and outputs the product matrix"""
'''I asked Chat GPT "what is wrong with my program?" multiple times.'''
'''The answer was usually "you have a syntax error" which was immediately obvious'''
'''when pointed out, but sometimes they were big syntax errors,'''
'''including a while loop in the wrong location that resulted in entire rows'''
'''appended to matrix B where single values were supposed to go'''
'''It also suggested enumerate() where a standard for loop was not working'''
'''This was for checking input and has been commented out, but it was important'''
'''for making sure the program was working correctly.'''


matrixA = []
matrixB = []
matrixC = []
def matrix_error():
    print(f"The input matrices cannot be multiplied! Rows of A not equal to columns of B!")
    exit()


if __name__ == '__main__':
    '''Get matrix A'''
    tokens = input("Enter values separated by spaces to populate a matrix \n"
                   "with a single row and any number of columns, then press enter.\n").split()
    for token in tokens:
        matrixA.append(int(token))
    #print(f"Matrix A =")
    #print(matrixA)
    num_columns = len(matrixA)
    #print(f"You entered {num_columns} values.")

    '''Get matrix B'''
    print(f"Enter values to populate a second matrix \n"
          f"with {num_columns} rows and {num_columns} columns.")
    for i in range(num_columns):
        matrixB_row = []
        tokens = input(f"Enter values separated by spaces for row {i+1}:\n").split()
        for token in tokens:
            matrixB_row.append(int(token))
        matrixB.append(matrixB_row)
    #print(f"Matrix B =")
    #for i in matrixB:
        #print(i)
    #print(f"You entered {len(matrixB)} rows with:")
    #for i, row in enumerate(matrixB):
        #print(f"{len(row)} values in row {i + 1}")

    '''Check if rows and columns of B equal rows of A'''
    if len(matrixB) != num_columns:
        matrix_error()
    for i in range(len(matrixB)):
        if len(matrixB[i]) != num_columns:
            matrix_error()


    '''Multiply matrix A by matrix B to get matrix C'''
    for i in range(num_columns):
        dot_product = 0
        for j in range (num_columns):
            dot_product += matrixA[j] * matrixB[j][i]
        matrixC.append(dot_product)

    print("Matrix A x Matrix B =")
    print(matrixC)