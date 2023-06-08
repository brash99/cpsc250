num = 585974156
base = 7

num_original = num
res = ""

digit_strings = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

while num > 0:
    digit = num % base
    # print(num, digit)
    res = digit_strings[digit]+res
    num = int(num/base)

print(num_original, " = ", res, " in base ", base)
