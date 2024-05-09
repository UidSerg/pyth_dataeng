import random


# Функция для проверки, можно ли разместить ферзя на данной позиции
def can_place(board, row, col):
    for i in range(row):
        if board[i] == col or \
                board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True


# Поиск всех решений рекурсивно
def place_queens(board, row, n):
    if row == n:
        return [board[:]]
    solutions = []
    for col in range(n):
        if can_place(board, row, col):
            board[row] = col
            for solution in place_queens(board, row + 1, n):
                solutions.append(solution)
    return solutions


# Генерации 4 случайных решений
def generate_solutions(n):
    board = [-1] * n
    solutions = place_queens(board, 0, n)
    return random.sample(solutions, 4)


# 4 случайных решения для проблемы 8 ферзей
solutions = generate_solutions(8)

# Итого
for i, solution in enumerate(solutions, 1):
    formatted_solution = [[i+1, col+1] for i, col in enumerate(solution)]
    print(f"Решение {i}: {formatted_solution}")