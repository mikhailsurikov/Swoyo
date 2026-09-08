from abc import abstractmethod


# Задание 5. Тарифы доставки
# Создайте родительский класс:
# Delivery
# Он принимает вес посылки и содержит метод:
# calculate()
# Создайте дочерние классы:
# StandardDelivery
# CourierDelivery
# ExpressDelivery
# Правила расчёта:
# StandardDelivery: 100 + вес * 20
# CourierDelivery: 300 + вес * 40
# ExpressDelivery: 500 + вес * 70
# Переопределите метод `calculate()`.
# После этого создайте список разных доставок и вызовите `calculate()` у каждой через один цикл.
# Тип объекта через `if` проверять не нужно.

class Delivery:
    """Посылка. Содержит информацию о весе посылки"""

    def __init__(self, weight):
        self.weight = weight

    @abstractmethod
    def calculate(self):
        """Расчет доставки"""
        pass


class StandardDelivery(Delivery):
    def calculate(self):
        return 100 + self.weight * 20


class CourierDelivery(Delivery):
    def calculate(self):
        return 300 + self.weight * 40


class ExpressDelivery(Delivery):
    def calculate(self):
        return 500 + self.weight * 70


deliveries = [
    StandardDelivery(5),
    CourierDelivery(5),
    ExpressDelivery(5)
]

for delivery in deliveries:
    print(delivery.calculate())
