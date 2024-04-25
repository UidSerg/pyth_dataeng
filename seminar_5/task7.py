"""
Создайте функцию-генератор. 
Функция генерирует N простых чисел, 
начиная с числа 2. 
Для проверки числа на простоту используйте правило: «число является простым, если делится нацело только на единицу и на себя».
"""
def prime(n):
    if n<3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def generate_simple(m):
    for i in range(2,m):
        if i > 200:
            raise StopIteration ()
        if prime(i):
            yield i

j = generate_simple(int(input("введите число N: ")))
for i in j:
    print(i, end=" ")