num = 0.95
num_original = num
p = 23

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

# print(num_original, " = ", "0.", res, " in binary.")
print(f"{num_original} = 0.{res} in binary.")
