# make matrix with A and B being the inputs and N being the amount of rows
# this collects data given splits it and lets me find out what N is
input_valuesAB = input()
input_lines_tot = input_valuesAB.splitlines()

N = len(input_lines_tot) # this itorated through the list and gives me N


# this will give me only the first row up until N colombs aid from chat gbt
matrix_A = [int(num) for num in input_lines_tot[0].split()]

#this should append input line total in to matrix B
matrix_B = []
matrix_B.append(input_lines_tot)


# makes c inally zero aid from stackoverflow should be [0, 0, 0, etc] making slots for the product of A and B
matrix_C = [0] * N
for x in range(N):
    for y in range(N):          #for loop should iterate through matrix A and B then multiply them then add them to the emply slots in C
        matrix_C = matrix_C + (matrix_A[x] * matrix_B[y])
        break
print(matrix_C)







