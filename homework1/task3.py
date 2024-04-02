"""
Программа загадывает число от 0 до 1000. 
Необходимо угадать число за 10 попыток. 
Программа должна подсказывать “больше” или “меньше” после каждой попытки.
Для генерации случайного числа используйте код:
from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)
"""
from random import randint
LOWER_LIMIT = 0
UPPER_LIMIT = 1000
count = 10

num = randint(LOWER_LIMIT, UPPER_LIMIT)

while count>0:
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