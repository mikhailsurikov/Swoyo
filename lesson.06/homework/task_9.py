# Задание 9 ⭐. Игровые персонажи
# Создайте родительский класс:
# Character
# Он принимает:
# * имя;
# * силу.
# Добавьте метод:
# attack()
# Создайте дочерние классы:
# Warrior
# Mage
# Archer
# Каждый класс должен по-своему рассчитывать силу атаки.
# ### Правила
# Воин:
# сила * 2
# Маг:
# сила * 3
# Лучник:
# сила + 10

class Character:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

    def attack(self):
        pass


class Warrior(Character):
    def attack(self):
        return f'{self.name.capitalize()} наносит {self.strength * 2} урона'


class Mage(Character):
    def attack(self):
        return f'{self.name.capitalize()} наносит {self.strength * 3} урона'


class Archer(Character):
    def attack(self):
        return f'{self.name.capitalize()} наносит {self.strength + 10} урона'


characters = [
    Warrior("Рагнар", 20),
    Mage("Мерлин", 20),
    Archer("Робин", 20)
]

for character in characters:
    print(character.attack())
