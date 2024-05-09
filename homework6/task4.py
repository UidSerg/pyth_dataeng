"""
Напишите функцию в шахматный модуль.
 Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
 Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
"""

import random
from task3 import queens_shess

__all__ = ['list_shess']

def list_shess(counts: int) -> list:
    list_correct = []
    while len(list_correct) < counts:
        queen_new = []
        for j in range(8):
            new_x = random.randint(1, 8)
            new_y = random.randint(1, 8)
            queen_new.append(list((new_x, new_y)))
        if queens_shess(queen_new) == True:
            list_correct.append(queen_new)
    return list_correct


if __name__ == '__main__':
    print("Удачные попытки расстановки: ")
    print(*list_shess(1), sep="\n") # формирование координат случайное по заданию. Лист из 4 возможных вариантов формируется очень долго

    # [[1, 4], [3, 5], [8, 2], [5, 1], [7, 8], [6, 6], [4, 3], [2, 7]]
    # [[8, 8], [1, 5], [6, 1], [4, 6], [2, 7], [5, 3], [7, 4], [3, 2]]
    # [[5, 3], [3, 2], [8, 4], [2, 7], [4, 6], [6, 1], [1, 5], [7, 8]]