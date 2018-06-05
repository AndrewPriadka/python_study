import random


def gen_matrix(n):
    matrix = []
    for i in range(n):
        line = []
        for j in range(n):
            line.append(random.randint(-10, 5))
        matrix.append(line)
    return matrix


m1 = gen_matrix(3)
m2 = gen_matrix(5)
