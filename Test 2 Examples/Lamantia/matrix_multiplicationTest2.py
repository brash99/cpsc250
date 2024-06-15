matrixA = []
matrixB = []
matrixC = []

class MatrixMultiplier:
    def __init__(self):
        self.matrixA = []
        self.matrixB = []
        self.matrixC = []

    def read_matrix(self):
        self.matrixA = list(map(int, input().strip().split()))
        N = len(self.matrixA)

        for i in range(N):
            row = list(map(int, input().strip().split()))
            if len(row) != N:
                print('The input matrices cannot be multiplied! Rows of A not equal to columns of B!')
                return False
            self.matrixB.append(row)

        return True

    def matrix_multiplication(self):
        N = len(self.matrixA)
        self.matrixC = [0] * N

        for i in range(N):
            sum_product = 0
            for j in range(N):
                sum_product += self.matrixA[j] * self.matrixB[j][i]
            self.matrixC[i] = sum_product

        return self.matrixC


if __name__ == "__main__":
    multiplier = MatrixMultiplier()

    if multiplier.read_matrix():
        result_matrix = multiplier.matrix_multiplication()
        print(" ".join(map(str, result_matrix)))
