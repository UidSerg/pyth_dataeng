"""
Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
 Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
   Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
"""

def prime(n):
    if n<2:
        return "составное"
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return "составное"
    return "простое"
n = int(input("введите число(1-100.000):"))
if 0 > n or n > 100000:
    print("Не верное число 1-100.000")
else:
    print(prime(n))
