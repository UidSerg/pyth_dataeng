"""
Добавьте в модуль с загадками функцию, которая хранит словарь списков. 
Ключ словаря - загадка, значение - список с отгадками. 
Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.
"""

def secrets(puzzle: str, answers: list[str], count=3) -> int:
    print(f'Угадай загадку.\n{puzzle}')
    for i in range(1, count+1):
        ans = input(f'Попытка номер {i}: ').lower()
        if ans in answers:
            return i
    return 0

if __name__ == '__main__':
    result = secrets('Зимой и летом одним цветом', ['ель', 'ёлка', 'сосна'])
    print(f'Угадал с {result} попытки' if result > 0 else 'Не угадал')

def storage():
    puzzles = {
        'Зимой и летом одним цветом': ['ель', 'ёлка', 'сосна'],
        'Не лает, не кусает, в дом не пускает': ['замок'],
        'Сидит дед во сто шуб одет': ['лук', 'луковица'],
    }
    for key, value in puzzles.items():
        result = secrets(key, value)
        print(f'Угадал с {result} попытки' if result > 0 else 'Не угадал')

if __name__ == '__main__':
    storage()


def save(puzzle: str, count: int):
    _data.update({puzzle: count})


def show():
    res = (f'Загадку "{key}" разгадали с {value}-й попытки' if value > 0
           else f'Загадку "{key}" не разгадали'
           for key, value in _data.items())
    print('\n'.join(res))