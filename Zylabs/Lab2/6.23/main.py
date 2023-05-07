def fibonacci(n):
    if n < 0:
        return -1
    if n == 0:
        return 0
    if n == 1:
        return 1
        
    last = 1
    before_last = 0
    for i in range(n):
        fib = last + before_last
        before_last = last
        last = fib
        
    return before_last


if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')
