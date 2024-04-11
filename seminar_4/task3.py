"""
Функция получает на вход строку из двух чисел через пробел. 
Сформируйте словарь, где ключом будет 
символ из Unicode, а значением —  целое число. 
Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.
"""
def unicode_range(text: str)-> dict:
    """Возвращает словарь символов.

    Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.
    """
    a,b = [int(i) for i in text.split()]
    return {chr(i):i for i in range(a,b+1)}


if __name__ == '__main__':
   text = input('Введите 2 числа: ')
   print(unicode_range(text)) 
