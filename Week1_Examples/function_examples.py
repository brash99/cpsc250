def add(a, b):
    c = a + b
    return c


x = 4
y = 6
z = add(x, y)
print(f"{x} + {y} = {z}")

x = "That is "
y = "so cool!"
z = add(x, y)
print(f"{x} + {y} = {z}")

x = 5.28
y = 6.23
z = add(x, y)
print(f"{x} + {y} = {z}")

x = True
y = False
z = add(x, y)
print(f"{x} + {y} = {z}")

employee_name = 'Bob'

# Note:  the function does not have any arguments passed
# to it

# Note:  the function does not pass any values back
# to the main program

def get_name():
    global employee_name
    name = input('Enter employee name:')
    employee_name = name
    return

get_name()
print(f"Employee name = {employee_name}")

# What happens when we pass a LIST to a function??????
# Hint:  something different than we might have expected!
numbers = [1, 2, 3, 4, 5]


def change_numbers(list_of_numbers):
    list_of_numbers[0] = 7
    return

change_numbers(numbers)
print(numbers)
