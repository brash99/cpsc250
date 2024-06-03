import sys

i = 45667

tf1 = True
tf2 = False

x = 32.446

myString1 = "A"
myString2 = "AB"
myString3 = "ABC"

print("Integer:")
print(sys.getsizeof(i), "bytes.")
print(id(i))

print("Boolean:")
print(sys.getsizeof(tf1), "bytes.")
print(sys.getsizeof(tf2), "bytes.")

print("Float:")
print(sys.getsizeof(x), "bytes.")

print("String:")
print(sys.getsizeof(myString1), "bytes.")
print(sys.getsizeof(myString2), "bytes.")
print(sys.getsizeof(myString3), "bytes.")