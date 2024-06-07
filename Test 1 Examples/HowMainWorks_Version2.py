from HowMainWorks_FunctionDefinitions import add, my_weird_function

if __name__ == "__main__":

    print("This is the main program: ", __name__)
    x = float(input("Type a number:"))
    y = float(input("Type another number:"))

    result = add(x,y)
    print(f"Add: {result}")

    result = my_weird_function(x,y)
    print(f"Weird Function: {result}")
