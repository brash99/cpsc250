def swap(a, b):
    temp = a
    a = b
    b = temp
    return

def swap_proper():
    global x,y

    temp = x
    x = y
    y = temp
    return

def swap_with_return(a, b):
    return b, a


if __name__ == "__main__":
    x = 5
    y = 10
    print(f"Before swap: x = {x}, y = {y}")
    swap(x, y)
    print(f"After swap: x = {x}, y = {y}")

    swap_proper()
    print(f"After proper swap: x = {x}, y = {y}")

    x, y = swap_with_return(x, y)
    print(f"After swap with return: x = {x}, y = {y}")