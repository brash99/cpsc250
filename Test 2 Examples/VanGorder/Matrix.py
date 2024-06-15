def matrix_mult(A, B):
    N = len(B)
    if len(A) != N:
        print('The input matrices cannot be multiplied! Rows of A not equal to columns of B!')
        return None

    C = [0] * N
    for j in range(N):
        for k in range(N):
            C[j] += A[k] * B[k][j]

    return C

def main():
    import sys
    input = sys.stdin.read().strip().split('\n')

    A = list(map(int, input[0].strip().split()))
    N = len(A)
    B = []
    for i in range(1, N+1):
        row = list(map(int,input[i].strip().split()))
        B.append(row)

    result = matrix_mult(A,B)
    if result is not None:
        print(' '.join(map(str,result)))
if __name__ == '__main__':
    main()

#used chatgbgt to help me with how to format the input statemnt to recieve an output


