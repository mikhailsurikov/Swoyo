# Задание 8 ⭐. Формирование отчёта из нескольких файлов
# Есть два файла.
# products.json
# {
#     "Ноутбук": 80000,
#     "Мышь": 2000,
#     "Монитор": 30000,
#     "Клавиатура": 5000
# }
# orders.csv
# Ноутбук,2
# Мышь,10
# Монитор,3
# Клавиатура,4
# Создайте программу, которая:
# 1. с помощью `pathlib` проверяет наличие обоих файлов;
# 2. загружает цены из JSON;
# 3. загружает количество проданных товаров из CSV;
# 4. вычисляет выручку по каждому товару;
# 5. создаёт папку `reports`, если её ещё нет;
# 6. сохраняет результат в:
# reports/report.txt
# ### Содержимое отчёта
# Ноутбук: 160000
# Мышь: 20000
# Монитор: 90000
# Клавиатура: 20000
# Общая выручка: 290000
# Самая большая выручка: Ноутбук
# Если `products.json` содержит некорректный JSON, обработайте:
# json.JSONDecodeError
# и выведите:
# Не удалось прочитать файл products.json
from pathlib import Path
import json
import csv


def my_func(json_file, csv_file):
    if not Path(json_file).exists():
        print(f"Файл {json_file} не существует")
    if not Path(csv_file).exists():
        print(f"Файл {csv_file} не существует")
    result = {}
    with open(json_file, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print(f'Не удалось прочитать файл {json_file}')
    with open(csv_file, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            result.update({row[0]: int(row[1]) * data.get(row[0], 1)})
    my_path = Path('reports/report.txt')
    with open(my_path, "w", encoding="utf-8") as f:
        f.writelines(f'{k}: {v}\n' for k, v in result.items())
        best_name = max(result, key=result.get)
        f.writelines(f'Общая выручка: {sum(result.values())},\nСамая большая выручка: {best_name}')


if __name__ == '__main__':
    json_file = 'products.json'
    csv_file = 'orders.csv'
    my_func(json_file, csv_file)
