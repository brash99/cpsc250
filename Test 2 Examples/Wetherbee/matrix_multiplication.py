def read_input():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')

    a = list(map(int, data[0].split()))
    b = [list(map(int, row.split())) for row in data[1:]]

    return a, b

def matrix_multiplication(a, b):
    if len(a) != len(b):
        return None

    n = len(a)
    c = [0] * n

    for i in range(n):
        for j in range(n):
            c[i] += a[j] * b[j][i]

    return c

def main():
    a, b = read_input()

    if len(b) != len(a):
        print("The input matrices cannot be multiplied! Rows of A not equal to columns of B!")
        return

    c = matrix_multiplication(a, b)

    if c is None:
        print("The input matrices cannot be multiplied! Rows of A not equal to columns of B!")
    else:
        print(' '.join(map(str, c)))

if __name__ == "__main__":
    main()
