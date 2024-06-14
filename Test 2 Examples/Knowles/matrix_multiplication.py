matrixA = []
matrixB = []
matrixC = []

def read_input():
    global matrixA, matrixB

#made these a global variable so that it will be easier to call back on them later in the code!!

    matrixA = list(map(int, input().strip().split())) #used map to apply the integer function to the elements in list created by .split!
    N = len(matrixA)

    for _ in range(N):
        row = list(map(int, input().strip().split())) #same method as used above ^^
        if len(row) != N:
            print("The input matricies cannot be multiplied! Rows of A are not equal to columns of B!")
            return False
        matrixB.append(row)
    return True

#This entire bit of code makes sure that the input by the user is something that the program can run - aka, if they put unequal rows and columns.

def multiply_matricies():
    global matrixA, matrixB, matrixC #this is creating a separate def. function for multiplying matricies, so created a new global variable for them.
    N = len(matrixA)
    matrixC = [0] * N #placeholder 0
    for i in range(N):
        for j in range(N):
            matrixC[i] += matrixA[j] * matrixB[j][i]  #multiplying the inputs of the user (hopefully matricies)

def main(): #here defines the actual code that will be used
    if read_input():
        multiply_matricies() #calling back the above function under main
        print(' '.join(map(str, matrixC))) #was unsure of how to get the formatting here, so used OpenAI assistance

if __name__ == '__main__':
    main()  #calling back the built in python main fuction
