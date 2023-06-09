import gc
import ctypes

gc_objs = gc.get_objects()
print(f"BEFORE: {len(gc_objs)}")


class Dog:
    def __init__(self, name):
        self.name = name


class Cat:
    def __init__(self, name, cousin=None):
        self.name = name
        self.cousin = cousin


bailey = Dog("Bailey")
misty = Cat("Misty")

print("\nREFERENCE COUNT")
print(f"bailey's reference count: {ctypes.c_long.from_address(id(bailey)).value}")
print(f"misty's reference count: {ctypes.c_long.from_address(id(misty)).value}")

gc_objs = gc.get_objects()
print(f"\nAFTER CREATION: {len(gc_objs)}")

del bailey
del misty

gc_objs = gc.get_objects()
print(f"\nAFTER DELETION: {len(gc_objs)}")
