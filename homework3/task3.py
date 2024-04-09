"""
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
 Не учитывать знаки препинания и регистр символов.
 За основу возьмите любую статью из википедии или из документации к языку.
"""
from collections import Counter
import re
from os import path

with open('text.txt', encoding='utf-8') as f:
    text = f.read()
text = re.sub(r"[^a-zA-Z]", " ", text)
new_text = text.split()
print(new_text)
print(Counter(new_text).most_common()[:10])

"""
text = input("Введите текст")
text = text.lower().replace(",", "").replace(".", "").replace("!", "").replace("?", "").replace("'"," ") # удаляем знаки препинания
new_text = text.split()
my_dict = {}
for i in new_text:
    if i.isdigit(): # если число
       pass
    else: 
        my_dict[i] = my_dict.get(i, 0) + 1 
sorted_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)

print(sorted_dict[:10])
"""


