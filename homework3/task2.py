"""
Дан список повторяющихся элементов.
Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
"""
lst = [1,2,3,4,5,6,8,8,8,9,7,6,5,4,3,2,1]
new_set = set(lst) # получим множество уникальных элементов
no_duble = []
for i in new_set:
    if lst.count(i) > 1: # если элемент уникального списка встречается  более 1 раза  добавляем  в список no_duble
        no_duble.append(i)
print(f'Список дублирующихся элементов: {no_duble}')