# Задание 3. Кошелёк
# Создайте класс:
# Wallet
# При создании передавайте количество денег.
# Реализуйте:
# __str__()
# __add__()
# При сложении двух кошельков должен создаваться новый объект `Wallet`, содержащий общую сумму.
# Исходные объекты изменяться не должны.

class Wallet:
    """
    Класс кошелек. 
    Хранит информацию о количество денег
    """

    def __init__(self, count):
        self.count = count

    def __str__(self):
        return f'Баланс: {self.count} руб'

    def __add__(self, other):
        if isinstance(other, Wallet):
            new_count = self.count + other.count
            return Wallet(count=new_count)


wallet1 = Wallet(1500)
wallet2 = Wallet(2300)
wallet3 = wallet1 + wallet2
print(wallet1)
print(wallet2)
print(wallet3)
