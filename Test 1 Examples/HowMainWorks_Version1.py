def add(x,y):
    print("This is the add function: ", __name__)
    return x + y

def my_weird_function(x,y):
    print("This is the my_weird_function function: ", __name__)
    return x**2/y**2*(x-y+4)

if __name__ == "__main__":

    print("This is the main program: ", __name__)
    x = float(input("Type a number:"))
    y = float(input("Type another number:"))

    result = add(x,y)
    print(f"Add: {result}")

    result = my_weird_function(x,y)
    print(f"Weird Function: {result}")
