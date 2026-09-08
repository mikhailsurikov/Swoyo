from functools import total_ordering


# Задание 4. Сравнение посылок
# Создайте класс:
# Parcel
# При создании передавайте:
# * название;
# * вес.
# Две посылки считаются равными, если их вес одинаковый.
# Также должна поддерживаться возможность сравнения:
# parcel1 < parcel2
# parcel1 > parcel2
# parcel1 <= parcel2
# parcel1 >= parcel2
# Реализуйте:
# __eq__()
# __lt__()
# и используйте:
# from functools import total_ordering
# Для упрощения считаем, что сравниваются только объекты `Parcel`.

@total_ordering
class Parcel:
    """Класс Посылка.
    Содержит название и вес посылки"""

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __lt__(self, other):
        return self.weight <= other.weight


parcel1 = Parcel("Книги", 4)
parcel2 = Parcel("Техника", 7)
parcel3 = Parcel("Одежда", 4)

print(parcel1 < parcel2)
print(parcel1 == parcel3)
print(parcel2 > parcel1)
