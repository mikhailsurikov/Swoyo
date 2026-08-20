# Задание 12 ⭐. Объединение остатков на складах
# Создайте новый словарь с общим количеством каждого товара на двух складах.

warehouse_1 = {
    "apple": 10,
    "banana": 5,
    "orange": 7
}
warehouse_2 = {
    "banana": 8,
    "orange": 3,
    "pear": 6
}
both_warehouses = {}
for k, v in warehouse_1.items():
    if k not in both_warehouses:
        both_warehouses.update({k: v + warehouse_2.get(k, 0)})
for k, v in warehouse_2.items():
    if k not in both_warehouses:
        both_warehouses.update({k: v + warehouse_1.get(k, 0)})
print(both_warehouses)

both_warehouses_2 = {}
for i in set(list(warehouse_1.keys()) + list(warehouse_2.keys())):
    both_warehouses_2.update({i: warehouse_1.get(i, 0) + warehouse_2.get(i, 0)})
print(both_warehouses_2)
