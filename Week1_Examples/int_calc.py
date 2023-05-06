def int_calc(x):
    prod = 1
    for i in range(2, x+1):
        prod = prod*i

    if x % 2 == 0:
        prod = prod + 100000
    else:
        prod = prod + 1000

    return prod


if __name__ == "__main__":
    print("int_calc(4)=", int_calc(4))
    print("int_calc(7)=", int_calc(7))
