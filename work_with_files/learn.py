# import os
# from pathlib import Path
# import json
# import csv
#
# # file = open('Документы/bytes.txt', encoding='utf-8')
# # print(file)
# # print(list(file))
# # file.close()
# #
# # file = open('Документы/text.txt', 'w', encoding='utf-8')
# # file.write('Я родился!)')
# # file.close()
#
# # file = open('Документы/bytes.txt', 'wb', buffering=64)
# # file.write(b'Hi i"m playing far cry3 MAAAAn!\nI"m Happy MANNN!')
# # file.close()
#
#
# # Операции с несколькими файлами
# # Неудобный способ
# # with open('Документы/text.txt', 'r', encoding='utf-8') as f, \
# #     open('Документы/bytes.txt', 'rb') as f2:
# #     print('-------------------')
# #     print(list(f))
# #     print(list(f2))
#
#
# # удобный
# # with (
# #     open('Документы/text.txt', 'r', encoding='utf-8') as f,
# #     open('Документы/text.txt', 'r', encoding='utf-8') as f2
# # ):
# #     print('------------------------')
# #     print(list(f))
# #     print(list(f2))
#
# # Чтение по заданной длине файла, а не полностью
# # SIZE = 4
# # with (
# #     open('Документы/text.txt', 'r', encoding='utf-8') as doc,
# # ):
# #     res = doc.read(7)
# #     print(res + '...')
# #
# # with open('Документы/bytes.txt', 'r') as doc1:
# #     for i in doc1:
# #         print(i)
#
# # Удаление созданных папки, если внутри пусто, модуль os
# # os.rmdir('Я папка')
# # Path('еще папка!').rmdir()
# # Path('i dir/dir in dir').rmdir()
#
# # Удаление папки с ее внутренностями
# # shutil.rmtree('i dir')
#
#
# # Создание папки
# # os.mkdir('Документы/Я папка')
# # Path('Документы/еще папка!').mkdir()
#
#
# # Создание вложенных папок
# # os.makedirs('i dir/dir in dir')
#
#
# # Переименование файла с os
# # os.rename('funny_scripts.py', 'bullshit_scripts.py')
# #
# # Path('bullshit_scripts.py').rename('funny_scripts.py')
#
# # Копирование всей папки
# # shutil.copytree('папка', 'др_папка')
#
#
# # Преобразование JSON в Python
# with open('Документы/person.json', 'r', encoding='utf-8') as file:
#     x = json.load(file)
#
# print(x)
# print(f"this is age: {x["age"]}")
# print(f"this firstname: {x['firstName']}")
#
# # Преобразование Python в JSON
# person = {
#     'name': 'Jack',
#     'surname': 'Wud',
#     'age': 17,
#     'job': 'Py-developer',
#     'address': {
#         'street': 'Central',
#         'city': 'Sidney',
#         'zipcode': '12375'
#     },
#     'phone': '+7-999-999-99-99'
# }
#
# with open('other_person.json', 'w', encoding='utf-8') as person_file:
#     json.dump(person, person_file, indent=2)
#
# # Преобразование в строку
# result = json.dumps(person, indent=2, separators=(',', ': '), sort_keys=True)
# print(result)
# print(type(result))
# print(result.count('surname'))
#
# # Создание csv-файла
# data = [
#     ["Name", "Age", "City"],
#     ["Alice", 30, "New York"],
#     ["Bob", 25, "Los Angeles"],
#     ["Charlie", 35, "Chicago"]
# ]
#
# with open('Документы/example.csv', mode="w", encoding="utf-8") as file:
#     writer = csv.writer(file)
#     writer.writerows(data)
#
# print(writer)
#
# # Чтение csv-файла
# with open('Документы/example.csv', 'r', encoding='utf-8', newline='') as f:
#     reader = csv.reader(f)
#     for i in reader:
#         print(i)
#     print(type(i))