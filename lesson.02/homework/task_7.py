# Задание 7. Добавление и изменение данных
# Добавьте товар `"pear"` с ценой `90`.
# После этого измените цену `"banana"` на `85`.

products = {
    "apple": 100,
    "banana": 80,
    "orange": 120}
products["pear"] = 90
products.update({"banana": 85})
print(products)
