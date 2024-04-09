"""
Создайте вручную кортеж содержащий элементы разных типов. 
Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа.
"""
tup = (12, "line 1", "line 2", 26.13, 1522, "line 3")

dict_type = {}

for item in tup:
    t = type(item).__name__
    if t not in dict_type:
        dict_type[t] = []
    dict_type[t].append(item)
print(dict_type)

## вариант 2

tpl = (1, 3.14, 'Hello', [1, 2, 3], 4, 5.6, 'Hi')

dct = {}
for element in tpl:
    if type(element).__name__ not in dct:
        dct[type(element).__name__] = [element]
    else:
        dct[type(element).__name__].append(element)

print(dct)