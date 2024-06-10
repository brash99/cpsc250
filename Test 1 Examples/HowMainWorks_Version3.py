import HowMainWorks_FunctionDefinitions as brashfunctions

if __name__ == "__main__":

    print("This is the main program: ", __name__)
    x = float(input("Type a number:"))
    y = float(input("Type another number:"))

    result = brashfunctions.add(x,y)
    print(f"Add: {result}")

    result = brashfunctions.my_weird_function(x,y)
    print(f"Weird Function: {result}")