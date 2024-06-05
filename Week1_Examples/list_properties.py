print("Python list: Basic storage model")

grades = [52, 55, 58, 61, 64]

# len(grades) = 5
# range(5) = [0, 1, 2, 3, 4]
# i will be 0, 1, 2, 3, 4
for i in range(len(grades)):
    address = id(grades[i])
    if i != 0:
        space = address - id(grades[i-1])
    else:
        space = 0
    print(i, grades[i], id(grades[i]), space)

print()

grades = [21, 34, 99, 100, 98]

for i in range(len(grades)):
    address = id(grades[i])
    if i != 0:
        space = address - id(grades[i-1])
    else:
        space = 0
    print(i, grades[i], id(grades[i]), space)

print()

grades = [21, 22, 23, 24, 25]

for i in range(len(grades)):
    address = id(grades[i])
    if i != 0:
        space = address - id(grades[i-1])
    else:
        space = 0
    print(i, grades[i], id(grades[i]), space)

print()
print("Conclusion:  the actual storage locations are not necessarily sequential ... Python is smarter than we are!")
print()

print("Python list methods:")

employee_info = ["John", "Smith", 1289, "Promenade Lane", 229724182]
print(employee_info)

employee_info.append("Software Developer")  # Add element to end
print(employee_info)

employee_info.remove("Promenade Lane")  # Remove specific element
print(employee_info)

employee_info.append("John")  # Add element to end (duplicate)
print(employee_info)

employee_info.remove("John")  # Remove specific element ... which one does it remove?
print(employee_info)
print()

#employee_info.sort()  # Note:  you will get an error here ... not all elements of the list are the same type!
#print(employee_info)

toppings = ['pepperoni', 'sausage', 'mushroom']
more_toppings = ['onion', 'bacon']
toppings.extend(more_toppings)  # Add elements from another list, one at a time ... note this is different from append
print(toppings)

toppings.pop()  # Remove element from the end of the list
print(toppings)
toppings.pop(1)  # Remove specific element, by index number
print(toppings)

toppings = ['pepperoni', 'sausage', 'mushroom', 'onion', 'bacon', 'anchovies', 'zebra']
toppings.sort()
print(toppings)  # sort in normal alphabetical order

toppings.sort(reverse=True)
print(toppings)  # sort in reverse alphabetical order

toppings.sort(reverse=True, key=lambda x: len(x))
print(toppings)  # sort by length of the word, largest to smallest


