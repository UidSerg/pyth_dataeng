"""
Создайте модуль с функцией внутри. 
Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток. 
Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток. 
Функция выводит подсказки “больше” и “меньше”. 
Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
"""
from random import randint

def guess_number(lover_limit, upper_limit, count):
    num = randint(lover_limit, upper_limit)

    while count > 0:
        n = int(input("Введите ваше число (0-1000): "))
        if num == n:
            print(f"Ура!!! это число {num} Вы угадали его с {10-count+1} раз")
            break
        else:
            if num > n: 
                print(f"Не угадали,загаданное число больше,осталось попыток {count-1}")
            else:
                print(f"Не угадали ,загаданное число меньше ,осталось попыток {count-1}")   
            count -=1
    print("GAME OVER")

if __name__ == '__main__':
    lover_limit, upper_limit, count = input('введите через пробел нижняя_граница верхняя_граница число_попыток: ').split()
    guess_number(int(lover_limit), int(upper_limit), int(count)) 

