"""
Напишите программу, которая получает целое число и возвращает 
его двоичное, восьмеричное строковое представление.
Функции bin и oct используйте для проверки своего 
результата, а не для решения.
Дополнительно:
Попробуйте избежать дублирования кода 
в преобразованиях к разным системам счисления
Избегайте магических чисел
Добавьте аннотацию типов где это возможно
"""
"""
BASE = 2
number1 = int(input("введите a:\n"))
number = number1
result = " "
while number > BASE:
    result += str(number%BASE)
    number //= BASE
result += str(number)
print(result[::-1])
print(bin(number1))

"""
"""
BASE = 8

number = int(input('Введите число: '))
print(oct(number))
result = ''
while number > BASE:
    result += str(number % BASE)
    number //= BASE
result += str(number)
print(result[::-1])
"""

def outnumber(number, base):
    result = ''
    while number > base:
        result += str(number % base)
        number //= base
    result += str(number)
    return result[::-1]

number = int(input('Введите число: '))
base = int(input('Введите систему исч 2/8: '))
print(outnumber(number, base))