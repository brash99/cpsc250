num = 0.95
p = 10

count = 0
res = ""

while num > 0 and count < p:
    comparison = 2**(-1-count)
    # print (num,comparison,res)
    if num > comparison:
        res = res + "1"
        num = num - comparison
    else:
        res = res + "0"

    count = count + 1

print(res)
