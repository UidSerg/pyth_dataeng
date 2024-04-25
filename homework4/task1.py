"""
Напишите функцию для транспонирования матрицы
"""


def transpon_matrix(matrix: list[list]) -> list[list]:
    """Функция транспонирует матрицу."""

    transpon_matrix = [[0 for i in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transpon_matrix[j][i] = matrix[i][j]
    return transpon_matrix        


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpon_matrix(matrix)
print(transpon_matrix(matrix))