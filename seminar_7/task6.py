"""
Дорабатываем функции из предыдущих задач. 
Генерируйте файлы в указанную директорию — отдельный параметр функции. 
Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки). 
Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
"""
# в task4 добавлено
"""
while True:
            try:
                with open(f'{directory}/{filename}.{extension}', 'x', encoding='utf-8') as f:
                    f.write(text)
            except:
                filename = generate_text(name_length)
            else:
                break
"""