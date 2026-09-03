# Задание 11 ⭐. Склад
# Создайте класс:
# Product
# У товара есть:
# * название;
# * цена;
# * количество.
# Также создайте класс:
# Warehouse
# Внутри него должен храниться список объектов `Product`.
# Добавьте методы:
# add_product(product)
# show_products()
# get_total_price()
# find_product(name)
# `get_total_price()` должен возвращать общую стоимость всех товаров:
# цена * количество

class Product:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

    def __repr__(self):
        return f'Название: {self.name}, Цена: {self.price}, Количество: {self.amount}'


class Warehouse:
    def __init__(self):
        self.warehouse = []

    def add_product(self, product):
        print(f'{product.name}: {product.amount} шт.')
        self.warehouse.append(product)

    def show_products(self):
        print(*self.warehouse, sep='\n')

    def find_product(self, name):
        for product in self.warehouse:
            if product.name == name:
                print(f'{product.name}: {product.amount} шт.')
                break
        else:
            print(f'{name} не найден')

    def get_total_price(self):
        print(f'Общая стоимость: {sum([product.amount * product.price for product in self.warehouse])}')


warehouse = Warehouse()

warehouse.add_product(Product("Ноутбук", 80000, 3))
warehouse.add_product(Product("Мышь", 2000, 10))
warehouse.add_product(Product("Монитор", 30000, 5))
warehouse.get_total_price()
warehouse.find_product("Монитор")
warehouse.show_products()
warehouse.find_product("Карандаш")
