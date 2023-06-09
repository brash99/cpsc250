class Test:

    def __init__(self, name):
        self.name = name
        print(f"... constructing {self.name} at {id(self.name)}")

    def __del__(self):
        print(f"... deleting {self.name}")


if "__name__" == "__name__":

    print("Part 1:")
    print("Discarded object creation")
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
