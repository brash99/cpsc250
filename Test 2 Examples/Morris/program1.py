def read_matrix():
    # Read the number of rows and columns for matrix a and b
    a = list(map(int, input("Enter the elements of matrix a separated by space: ").strip().split()))
    n = len(a)

    b = []
    print(f"Enter the elements of matrix b row by row (each row should have {n} elements):")
    for i in range(n):
        row = list(map(int, input().strip().split()))
        if len(row) != n:
            print("The input matrices cannot be multiplied! Rows of A not equal to columns of B!")
            return None, None
        b.append(row)

    return a, b


def validate_matrices(a, b):
    # Check if the number of columns in a matches the number of rows in b
    if a is None or b is None:
        return False
    if len(a) != len(b):
        print("The input matrices cannot be multiplied! Rows of A not equal to columns of B!")
        return False
    return True


def multiply_matrices(a, b):
    # Perform matrix multiplication
    n = len(a)
    c = []
    # Iterate over each column of b
    for i in range(n):
        total = 0
        # Compute the dot product of a's row with b's column
        for j in range(n):
            total += a[j] * b[j][i]
        # Append the result to the output matrix c
        c.append(total)
    return c


def main():
    # Read matrices a and b from input
    a, b = read_matrix()

    # Validate the matrices dimensions
    if not validate_matrices(a, b):
        return

    # Multiply matrices and get the result
    c = multiply_matrices(a, b)

    # Print the resulting matrix c
    print(' '.join(map(str, c)))


if __name__ == "__main__":
    main()
