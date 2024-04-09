"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
 Программа должна возвращать сумму и произведение* дробей.
   Для проверки своего кода используйте модуль fractions
"""

from fractions import Fraction
import re # для проверки строки на формат дроби

frac1 = input("введите дробь в формате (a/b): ")
frac2 = input("введите дробь в формате (a/b): ")
parts1 = re.split('/', frac1)
parts2 = re.split('/', frac2)
if len(parts1) != 2: # формат дроби а/б идем дальше только если 2 части
  print("В первом случае введена не дробь")
if len(parts2) != 2:
  print("Во втором случае введена не дробь")
else:
  drob1 = frac1.split(sep ='/')
  drob2 = frac2.split(sep ='/')
  if (drob1[0].isdigit() and drob1[1].isdigit() and drob2[0].isdigit() and drob2[1].isdigit()):  #проверка на число в каждой части split
    chisl = int(drob1[0]) * int(drob2[1]) + int(drob2[0]) * int(drob1[1])
    znam = int(drob1[1]) * int(drob2[1])
    rezult = str(chisl) + '/' + str(znam)
    proizv = str(int(drob1[0])*int(drob2[0])) + '/' + str(int(drob1[1])*int(drob2[1]))
    print(f'Сумма дробей: {rezult}')
    print(f'Произведение дробей: {proizv}')
  else:
    print('в одной из строк числитель/ знаменатель не число!!!')

## проверка с помощью функции Fraction
x = Fraction(frac1)
y = Fraction(frac2)
print("Проверка функцией Fraction: ")
print(f'Сумма дробей: {x+y}')
print(f'Произведение дробей: {x*y}')


