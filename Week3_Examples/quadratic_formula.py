import math

if __name__ == '__main__':

    a = 1.0
    b = 5.0
    c = 0.0

    root1 = (-b + math.sqrt(b ** 2 - 4.0 * a * c)) / (2.0 * a)
    root2 = (-b - math.sqrt(b ** 2 - 4.0 * a * c)) / (2.0 * a)

    print(root1, root2)
