# Задание 6. Туристический дрон
# Создайте два независимых класса:
# CameraModule
# NavigationModule
# `CameraModule` содержит:
# take_photo()
# `NavigationModule` содержит:
# build_route(city)
# Создайте класс:
# TravelDrone
# который наследуется одновременно от `CameraModule` и `NavigationModule`.
# Сам дрон должен иметь название и метод:
# fly()

class CameraModule:
    """Камера"""

    def take_photo(self):
        return 'Фотография сделана'


class NavigationModule:
    """Навигатор"""

    def build_route(self, city):
        return f'Маршрут построен до: {city}'


class TravelDrone(CameraModule, NavigationModule):
    """Дрон путешественник"""

    def __init__(self, name):
        self.name = name

    def fly(self):
        return f'{self.name} начал полёт'


drone = TravelDrone("Explorer")

print(drone.fly())
print(drone.take_photo())
print(drone.build_route("Сочи"))
