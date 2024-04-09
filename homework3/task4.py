"""
4. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
 Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
 Достаточно вернуть один допустимый вариант.*Верните все возможные варианты комплектации рюкзака.
"""
# *Верните все возможные варианты комплектации рюкзака.

import random

things = {
    "спальник": 1.5,
    "палатка": 3.2,
    "термос": 0.6,
    "карта": 0.1,
    "фонарик": 0.3,
    "котелок": 0.8,
    "еда": 2.5,
    "одежда": 1.7,
    "обувь": 1.2,
    "нож": 0.5
}

list_keys= [] # создадим лист из ключей
for key in things.keys():
    list_keys.append(key)

max_weight = 7.0
backpack = {}
weight = 0

while len(list_keys) > 0:  # пока лист из ключей не пустой, берем случайный предмет проверяем меньше ли он оставшегося веса
    key_exit = random.choice(list_keys)
    if max_weight - things[key_exit] >= 0:
        max_weight -= things[key_exit]
        backpack[key_exit] = things[key_exit] # закидываем рюкзак
        weight += things[key_exit]
    else: # иначе выкидываем
        pass
    list_keys.remove(key_exit) # в любом случае удаляем из листа ключей

print(f'В рюкзак влезли {backpack} массой {weight}')
"""
#  Достаточно вернуть один допустимый вариант

backpack = {}
count = 0
for k in things:
   if max_weight - (count+things[k]) >= 0:
        backpack[k] = things[k]
        count += things[k]
        print(count)
print(backpack)
"""