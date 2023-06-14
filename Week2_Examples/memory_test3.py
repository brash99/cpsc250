import ctypes
#import tracemalloc


class Dog:
    def __init__(self, name, cousin=None):
        self.name = name
        self.cousin = cousin


class Cat:
    def __init__(self, name, cousin=None):
        self.name = name
        self.cousin = cousin


#tracemalloc.start(5)
#time1 = tracemalloc.take_snapshot()

bailey = Dog("Bailey")  # create bailey, with no cousins
misty = Cat("Misty", bailey)  # create misty, assign bailey as her cousin
bailey.cousin = misty  # assign misty as bailey's cousin

print("\nREFERENCE COUNT after creation of bailey and misty")
print(f"bailey's reference count: {ctypes.c_long.from_address(id(bailey)).value}")
print(f"misty's reference count: {ctypes.c_long.from_address(id(misty)).value}")

del bailey

print("\nREFERENCE COUNT after deletion of bailey")
print(f"misty's reference count: {ctypes.c_long.from_address(id(misty)).value}")

misty.cousin = None

print("\nREFERENCE COUNT after deletion of bailey")
print(f"misty's reference count: {ctypes.c_long.from_address(id(misty)).value}")

del misty

# time2 = tracemalloc.take_snapshot()
# stats
# stats = time2.compare_to(time1, "lineno")
# for stat in stats[:3]:
#    print(stat)
