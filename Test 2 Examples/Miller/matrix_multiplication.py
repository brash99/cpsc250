def read_input():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')

    # Read matrix A
    a_matrix = list(map(int, data[0].split()))

    # making sure there are enough rows for matrix B
    if len(data) != len(a_matrix) + 1:
        return a_matrix, None

    # Read matrix B
    b_matrix = [list(map(int, data[i + 1].split())) for i in range(len(a_matrix))]

    return a_matrix, b_matrix

# Used Github Copilot assistance through-out the code
def validate_input(a_matrix, b_matrix):
    if b_matrix is None:
        return False
    n = len(a_matrix)
    if n != len(b_matrix):
        return False
    for row in b_matrix:
        if len(row) != n:
            return False
    return True

# Multiplying the matrixes
def multiply_matrices(a_matrix, b_matrix):
    n = len(a_matrix)
    c_matrix = [0] * n
    for i in range(n):
        for j in range(n):
            c_matrix[i] += a_matrix[j] * b_matrix[j][i]
    return c_matrix

# Used the help of Copilot and ChatGPT
def swoop():
    a_matrix, b_matrix = read_input()

    if not validate_input(a_matrix, b_matrix):
        print("The input matrices cannot be multiplied! Rows of A not equal to columns of B!")
        return

    c_matrix = multiply_matrices(a_matrix, b_matrix)
    print(" ".join(map(str, c_matrix)))


if __name__ == "__main__":
    swoop()


