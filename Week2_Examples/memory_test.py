class Test:

    def __init__(self, name):  # Constructor Method
        self.name = name
        print(f"... constructing {self.name} at {id(self.name)}")

    def __del__(self):  # Destructor Method!!! Called by Garbage Collector
        print(f"... deleting {self.name}")


if "__name__" == "__name__":

    print("Part 1:")
    print("Discarded object creation")
    # create an object "hello1", but don't assign it to anything
    # expect creation, followed by immediate destruction
    Test("hello1")

    print("Saved object creation")
    myList = Test("hello2")

    print("Part 2:")

    s1 = Test("Python")
    s2 = Test("Computer Science")
    s3 = s2
    s1 = Test("Zybooks")
    s2 = s1
    s3 = s1

    print("program done")
