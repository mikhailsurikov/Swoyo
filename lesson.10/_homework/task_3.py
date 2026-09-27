# Задание 3. Работа с путями
# Используя `pathlib`, создайте структуру:
# reports/
#     2026/
#         september/
# В папке `september` создайте файл:
# result.txt
# и запишите в него:
# Отчёт сформирован
# После этого выведите:
# * имя файла;
# * родительскую папку;
# * существует ли файл;
# * является ли путь файлом;
# * абсолютный путь.
from pathlib import Path
import os

my_path = Path('./reports/2026/september/result.txt')
os.makedirs(os.path.dirname(my_path), exist_ok=True)
with open(my_path, mode='w', encoding='utf-8') as file:
    file.write('Отчёт сформирован')

print(f'Имя: {my_path.name}')
print(f'Родитель: {my_path.parent}')
print(f'Существует: {my_path.exists()}')
print(f'Это файл: {my_path.is_file()}')
print(f'Абсолютный путь: {my_path.absolute()}')
