# Using built-in function
num = 4095
num = 34596
b = bin(num)
print(f"Built-in Function: {num} = {b} in binary.")

# Using custom function
num_original = num
result = ""

while num > 0:
    digit = num % 2
    num = int(num/2)
    # print(num, digit)
    result = str(digit)+result

print(f"Custom Function:   {num_original} = 0b{result} in binary.")
