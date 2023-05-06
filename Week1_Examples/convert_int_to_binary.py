num = 13
res = ""

while num > 0:
    digit = num % 2
    print(num, digit)
    res = str(digit)+res
    num = int(num/2)

print()
print(res)
