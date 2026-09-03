# Задание 6. Доставка посылок
# Создайте родительский класс:
# Delivery
# При создании передавайте:
# * город;
# * вес посылки.
# Добавьте метод:
# calculate_price()
# Создайте два дочерних класса:
# CourierDelivery
# PostDelivery
# Переопределите метод `calculate_price().
# Курьерская доставка:
# 500 + 50 * вес
# Почтовая доставка:
# 200 + 30 * вес

class Delivery:
    def __init__(self, city, weight):
        self.city = city
        self.weight = weight

    def calculate_price(self):
        pass


class CourierDelivery(Delivery):

    def calculate_price(self):
        return 500 + 50 * self.weight


class PostDelivery(Delivery):

    def calculate_price(self):
        return 200 + 30 * self.weight


courier = CourierDelivery("Москва", 3)
post = PostDelivery("Казань", 3)

print(courier.calculate_price())
print(post.calculate_price())

delivery_list = [CourierDelivery("Нижний Новгород", 20), PostDelivery("Тула", 7), CourierDelivery("Сочи", 13)]
print(*[i.calculate_price() for i in delivery_list])
