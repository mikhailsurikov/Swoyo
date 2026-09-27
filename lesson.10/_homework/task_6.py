# Задание 6. Анализ продаж из CSV
# Создайте файл:
# sales.csv
# Содержимое:
# Ноутбук,2,80000
# Мышь,5,2000
# Монитор,3,30000
# Клавиатура,4,5000
# Каждая строка содержит:
# товар, количество, цена
# Прочитайте файл с помощью `csv.reader()`.
# Определите:
# 1. общую сумму продаж;
# 2. товар, проданный в наибольшем количестве.
import csv

rows = [
    ["Ноутбук", "2", "80000"],
    ["Мышь", "5", "2000"],
    ["Монитор", "3", "30000"],
    ["Клавиатура", "4", "5000"],
]
file_name = 'sales.csv'
with open(file_name, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

total_sum = 0
max_quantity = -1
best_item = None

with open(file_name, 'r', newline='', encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        item = row[0]
        quantity = int(row[1])
        price = int(row[2])
        total_sum += quantity * price
        if quantity > max_quantity:
            max_quantity = quantity
            best_item = item

print(f"Общая сумма продаж: {total_sum}")
print(f"Больше всего продано: {best_item}")
print(f"Количество: {max_quantity}")
