import numpy as np

# Definindo as matrizes A, B e C
A = np.array([[2, -25, 12, 6],
              [5, -5, 8, -5],
              [12, 6, 5, 9],
              [5, -1, -40, 11],
              [7, 9, 7, -4]])

B = np.array([[2, -1, 6, -6, 1],
              [-10, 12, 8, 14, 5],
              [9, -7, 6, 5, 8],
              [1, -3, -9, 4, -2]])

C = np.array([[2, 5, 0, 1, 4],
              [3, -9, 7, 3, 6],
              [10, 5, -2, 4, -8],
              [-3, 2, 1, 4, 2]])

# Calculando a matriz M = AB
M = np.dot(A, B)

# Calculando a matriz N = B + C
N = B + C

# a) Calculando m43 + n34
a = M[3, 2] + N[2, 3]

# b) Calculando m35 - 3*n23
b = M[3, 4] - 3 * N[1, 2]

print("a) m43 + n34 =", a)
print("b) m35 - 3*n23 =", b)
