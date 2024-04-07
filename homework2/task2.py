"""
Напишите программу,
 которая получает целое число и возвращает его шестнадцатеричное строковое представление.
 Функцию hex используйте для проверки своего результата.
"""

def outnumber(number, base):
    number_str = '0123456789ABCDEF'
    result = ''
    while number > base:
        if base == 16:
            result += number_str[number % base]
        else:
            result += str(number % base)    
        number //= base
    if base == 16:
        if number  == base:
            result += str("01")
        else:    
            result += number_str[number]
    else:
        result += str(number)
    return result[::-1]

number = int(input('Введите число: '))
base = int(input('Введите систему исч 2/8/16: '))
print(outnumber(number, base))
print(hex(number))
print(oct(number))
print(bin(number))