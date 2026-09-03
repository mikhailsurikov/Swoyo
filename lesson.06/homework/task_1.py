# Задание 1. Книга
# Создайте класс:
# Book
# При создании книги передавайте:
# * название;
# * автора;
# * количество страниц.
# Добавьте метод:
# show_info()

class Book:
    def __init__(self, name, author, page_count):
        self.name = name
        self.author = author
        self.page_count = page_count

    def show_info(self):
        print(f'Название: {self.name} \nАвтор: {self.author}\nСтраниц: {self.page_count}')


book = Book("1984", "Джордж Оруэлл", 328)
book.show_info()
