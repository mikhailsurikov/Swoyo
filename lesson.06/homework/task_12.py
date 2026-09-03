# Задание 12 ⭐. Система заказов
# Создайте родительский класс:
# Order
# При создании передавайте:
# * номер заказа;
# * стоимость товаров.
# Стоимость храните в приватном атрибуте:
# __price
# Добавьте методы:
# get_price()
# set_price(price)
# get_total()
# show_info()
# Цена не может быть отрицательной.
# Создайте три дочерних класса:
# PickupOrder
# CourierOrder
# ExpressOrder
# Переопределите метод:
# get_total()
# ### Правила расчёта
# Самовывоз:
# стоимость товаров
# Курьерская доставка:
# стоимость товаров + 500
# Экспресс-доставка:
# стоимость товаров + 1000
# Создайте список разных заказов:
# С помощью одного цикла:
# 1. выведите номер каждого заказа;
# 2. выведите итоговую стоимость;
# 3. с помощью `isinstance()` определите способ получения заказа;
# 4. посчитайте общую стоимость всех заказов.

class Order:
    def __init__(self, number, price):
        self.number = number
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price < 0:
            print('Цена не может быть отрицательной')
        else:
            self.__price = price

    def get_total(self):
        return self.__price * self.number

    def show_info(self):
        print(f"Номер заказа: {self.number}. Стоимость: {self.__price}")


class PickupOrder(Order):
    def get_total(self):
        return self.get_price()

    def __repr__(self):
        return "Самовывоз"


class CourierOrder(Order):
    def get_total(self):
        return self.get_price() + 500

    def __repr__(self):
        return "Курьерская доставка"


class ExpressOrder(Order):
    def get_total(self):
        return self.get_price() + 1000

    def __repr__(self):
        return "Экспресс доставка"


orders = [
    PickupOrder(101, 5000),
    CourierOrder(102, 3000),
    ExpressOrder(103, 10000),
    CourierOrder(104, 7000)
]

total_sum = 0
for order in orders:
    print(f'Заказ №{order.number}')
    print(order)
    print(f'Итого: {order.get_total()}\n')
    total_sum += order.get_total()
print(f'Общая сумма: {total_sum}')
