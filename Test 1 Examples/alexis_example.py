def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

def my_weird_function(x,y):
    return x**2/y**2*(x-y+4)

def make_things(wood, glue, nails):

    chair = wood + glue + nails
    table = wood + 2*glue + 4*nails

    return (chair, table)

# Start the main program
if __name__ == '__main__':

    # now we are in the main program

    # Step #1: Input two numbers - one on each line
    #
    # 3.14
    # 2.71
    x = float(input())
    y = float(input())

    # Step #1:
    result = add(x,y)
    print(f"Add: {result}")

    # Step #2:
    result = my_weird_function(x,y)
    print(f"Weird Function: {result}")

    my_wood = 10
    my_glue = 2
    my_nails = 16

    # Step #3: Make things
    # bob and fred are the values of chair and table that are returned
    # from the make_things function
    bob, fred = make_things(my_wood, my_glue, my_nails)
    print(f"Chair: {bob}")
    print(f"Table: {fred}")

    # what if we have a bunch of numbers on ONE line of input?
    #
    # 10 2 16

    line = input()       # line = "10 2 16"
    parts = line.split() # parts = ["10", "2", "16"]
    parts_numbers = [int(x) for x in parts] # parts_numbers = [10, 2, 16]

    # Step #4: Make things again
    # bob and fred are the values of chair and table that are returned
    # from the make_things function

    bob, fred = make_things(parts_numbers[0], parts_numbers[1], parts_numbers[2])
    print(f"Chair: {bob}")
    print(f"Table: {fred}")





