"""
4. Создайте функцию генератор чисел Фибоначчи
https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8
"""
"""
def fibonachi(n:int):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonachi(n-1)+fibonachi(n-2)


n = int(input('Введите необходимое число чисел последовательности Фибоначчи: '))
list_compl = [fibonachi(i) for i in range(1, n+1)]
print(list_compl)
"""

def fibonachi(n: int):
    """Генератор чисел Фибоначчи."""
    a, b = 0, 1
    yield a
    yield b
    for _ in range(n-2):
        yield a + b
        a, b = b, a + b


n = int(input('Введите необходимое число чисел последовательности Фибоначчи: '))
res = [i for i in fibonachi(n)]
print(res)
