# Задание 15 ⭐. Статистика магазина
# Дан словарь с количеством проданных товаров
# И словарь с ценами
# Необходимо:
# 1. посчитать общую выручку магазина;
# 2. найти товар, который продали в наибольшем количестве;
# 3. найти товар, который принёс наибольшую выручку.

sales = {
    "Ноутбук": 7,
    "Мышь": 25,
    "Клавиатура": 14,
    "Монитор": 9,
    "Наушники": 18
}
prices = {
    "Ноутбук": 85000,
    "Мышь": 3500,
    "Клавиатура": 7200,
    "Монитор": 32000,
    "Наушники": 11500
}
sum_sales = 0
for i in sales:
    sum_sales += sales.get(i) * prices.get(i)
print(f'Общая выручка: {sum_sales}')
max_sales = ''
for k, v in sales.items():
    if v == max(sales.values()):
        max_sales = k
print(f'Больше всего продано: {max_sales}\nКоличество: {max(sales.values())}')
revenue = {}
for i in sales:
    revenue.update({i: sales.get(i) * prices.get(i)})
max_revenue = ''
for k, v in revenue.items():
    if v == max(revenue.values()):
        max_revenue = k
print(f'Наибольшая выручка: {max_revenue}\nВыручка: {max(revenue.values())}')
