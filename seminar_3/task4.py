"""
Создайте вручную список с повторяющимися элементами.
Удалите из него все элементы, которые встречаются дважды.
"""
from collections import Counter

lst = [1,2,3,4,5,5,5,8,6,7,6,5,4,3,2,1]
dic2 = Counter(lst)
dic = {}
for item in lst:
    if item not in dic:
        dic[item] =0
    dic[item] +=1 ## dct[el] = dct.get(el, 0) 
for k,v in dic.items():
    if v == 2:
        lst.remove(k) # удаляет только одно вхожденне
        lst.remove(k)    
print(lst)
print(dic)
print(dic2)