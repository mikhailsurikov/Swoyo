# Задание 4. Игровой инвентарь
# Создайте класс:
# Inventory
# Внутри объекта должен храниться список предметов:
# self.items = []
# Добавьте методы:
# add_item(item) добавляет предмет.
# remove_item(item) удаляет предмет, если он существует.
# has_item(item) возвращает `True` или `False`
# show_items() выводит все предметы.

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def has_item(self, item):
        return item in self.items

    def show_items(self):
        print(*self.items, sep='\n')


inventory = Inventory()

inventory.add_item("меч")
inventory.add_item("щит")
inventory.add_item("зелье")

inventory.remove_item("щит")

inventory.show_items()

print(inventory.has_item("меч"))
print(inventory.has_item("лук"))
