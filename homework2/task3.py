"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
 Программа должна возвращать сумму и произведение* дробей.
   Для проверки своего кода используйте модуль fractions
"""

from fractions import Fraction

frac1 = input("введите дробь в формате (a/b): ")
frac2 = input("введите дробь в формате (a/b): ")

drob1 = frac1.split(sep ='/')
drob2 = frac2.split(sep ='/')

chisl = int(drob1[0]) * int(drob2[1]) + int(drob2[0]) * int(drob1[1])
znam = int(drob1[1]) * int(drob2[1])
rezult = str(chisl) + '/' + str(znam)


proizv = str(int(drob1[0])*int(drob2[0])) + '/' + str(int(drob1[1])*int(drob2[1]))

print(f'Сумма дробей: {rezult}')
print(f'Произведение дробей: {proizv}')

## проверка с помощью функции Fraction
x = Fraction(frac1)
y = Fraction(frac2)
print("Проверка функцией Fraction: ")
print(f'Сумма дробей: {x+y}')
print(f'Произведение дробей: {x*y}')

