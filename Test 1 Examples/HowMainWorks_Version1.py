def add(x,y):
    print("This is the add function: ", __name__)
    return x + y

def my_weird_function(x,y):
    print("This is the my_weird_function function: ", __name__)
    return x**2/y**2*(x-y+4)

MY_CONSTANT = 3.14159

if __name__ == "__main__":

    print("This is the main program: ", __name__)

    x = float(input("Type a number:"))
    y = float(input("Type another number:"))

    result = add(x,y)
    print(f"Add: {result}")

    # now, both numbers input on the SAME LINE!!!
    # for example:
    # 3.14 2.71

    # The multi-step way:
    # line = input()       # line = "3.14 2.71"
    # parts = line.split() # parts = ["3.14", "2.71"]
    # x = float(parts[0])  # x = 3.14
    # y = float(parts[1])  # y = 2.71

    # List comprehension is a way to create a list in one line
    x, y = [float(x) for x in input().split()]

    result = my_weird_function(x,y)
    print(f"Weird Function: {result}")
