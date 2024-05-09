"""
2. Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
 Результаты обхода сохраните в файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
"""

import os
import json
import csv
import pickle



directory = "./homework8"
list_dicts= []
for dir_path, dir_name, file_name, in os.walk(directory):
    save_dict = {}
    save_dict["Name"] = dir_path.split('\\')[-1]
    save_dict["parents_dir"]  = dir_path[:-len(dir_path.split('\\')[-1])]
    save_dict["dir_size"] = sum(os.path.getsize(os.path.join(dir_path, name)) for name in file_name) 
    dict_dir = {} # словарь вложенных папок
    for i in range(len(dir_name)):
        dict_dir[dir_name[i]] = dir_name[i]
    save_dict["dirs"] = [dict_dir]
    dict_file = {} # словарь вложенных файлов
    for i in range(len(file_name)):
        dict_file[file_name[i]] = os.path.getsize(os.path.join(dir_path,file_name[i]))
    save_dict["files"] = [dict_file]
    list_dicts.append(save_dict)
with open('home8.json', 'w', encoding='utf-8') as f:
        json.dump(list_dicts, f, indent=4, separators=(',', ':'))

## откроем json, запишем в pickle
with open('home8.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
with open('home8.pickle', 'wb') as f:
    pickle.dump(data, f)

## запись в CSV
with open('home8.csv', 'w', newline='', encoding='utf-8') as f_write:
    keys = ['Name','parents_dir','dir_size','dirs','files']
    csv_write = csv.DictWriter(f_write, fieldnames=keys, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)    
    csv_write.writeheader()
    csv_write.writerows(list_dicts)
  