"""
2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
 где ключ — значение переданного аргумента, а значение — имя аргумента.
   Если ключ не хешируем, используйте его строковое представление.
"""


def my_dict(**kwargs):
  d = {}
  s = set()
  for key, value in kwargs.items():
    try:
      s.add(value)
    except:
      value = str(value)
    d[value] = key
  return d

print(my_dict(x=1, y=2, z=3))

