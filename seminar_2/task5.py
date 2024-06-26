"""
Напишите программу, которая решает квадратные уравнения даже если 
дискриминант отрицательный. 
Используйте комплексные числа 
для извлечения квадратного корня.
"""

a = int(input("введите a:\n"))
b = int(input("введите b:\n"))
c = int(input("введите c:\n"))

d = b**2 - 4*a*c
if d > 0:
    print((-b+d**0.5)/(2*a))
    print((-b-d**0.5)/(2*a))
elif d == 0:
    print((-b)/(2*a))  
else:
    d = complex(d)
    print((-b+d**0.5)/(2*a))
    print((-b-d**0.5)/(2*a))