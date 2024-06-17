#matrixA = input()
#matrixB = input()
#matrixC = input()

matrixA = input().split() #spliting each one into individual numbers
matrixB = input().split()
matrixC = input().split()

#matrixA = int(matrixA) #tried to make the marticies into int so i could iterate through, but it didnt like that
#matrixB = int(matrixB)

num_rows = len(matrixA) #got their lengths so i could iterate through their length in loops
num_rcB = len(matrixB)
#num_c = len(matrixC)


#print(num_rows) #error testing
#print(num_rcB)

#this is my attempt, i got it to give me some sort of output during one of my trials, but i changed something
#slightly and couldnt get that trial to give me what i had gotten out of it previously

if num_rows != num_rcB: #if the numbers dont equal each other, print:
    print('The input matrices cannot be multiplied! Rows of A not equal to columns of B!')
elif num_rows == num_rcB: #if they do equal each other:
    for i in num_rows: #for each number within num_rows
        for j in num_rcB: #for each number in num_rcB
            for i in j : #and then for each number in each number from each row:
                print(i*j) #multiply them

#these were my previous attempts, which wouldnt really output anything:
'''
#while True:  #trying tp figure out how to iterate thru each row and column
if num_rows >= 1 and num_rcB >=1 :
    for i in range(num_rows): #using the range() was ai, i didnt know that using range() within the
        for j in range(num_rcB): #for loops would make it run through the number
            print(j*(i*j))



for i in matrixA:
    for j in matrixB:
        print(i*j)
'''
