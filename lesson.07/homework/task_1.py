# Задание 1. Фильм
# Создайте класс:
# Movie
# При создании фильма передавайте:
# * название;
# * год выпуска;
# * рейтинг.
# Реализуйте методы:
# __str__()
# __repr__()
# `__str__()` должен возвращать удобное представление фильма для пользователя.
# `__repr__()` должен показывать основные данные объекта.

class Movie:
    """
    Класс Фильм.
    Содержит информацию: название, год выпуска, рейтинг
    """
    def __init__(self, name, year, rating):
        self.year = year
        self.name = name
        self.rating = rating

    def __str__(self):
        return f"{self.name} ({self.year}), рейтинг: {self.rating}"

    def __repr__(self):
        return f'Movie("{self.name}", {self.year}, {self.rating})'


movie = Movie("Интерстеллар", 2014, 8.7)

print(movie)
print([movie])
