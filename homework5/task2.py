"""
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""


def file_path(text: str):
    """Функция возвращает кортеж из трёх элементов: путь, имя файла
      расширение файла.
    """

    *_, file = text.split('/')
    *_, extension = file.split('.')
    file_name = file[:-(len(extension)+1)]
    url = text[:-(len(file)+1)]
    return url, file_name, extension


if __name__ == '__main__':
    text = "https://proprikol.ru/wp-content/uploads/2020/02/porodistye-sobaki-krasivye-kartinki-31.jpg"
    text1 = "e:/Рабочий стол/Gb/python_dataeng/pyth_dataeng/homework5/task1.py"
    text2 = "e:/Рабочий стол/Gb/python_dataeng/pyth_dataeng/homework5/task1-31.jpg.py"
    print(file_path(text))
    print(file_path(text1))
    print(file_path(text2))
