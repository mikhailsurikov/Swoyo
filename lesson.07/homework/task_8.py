# Задание 8 ⭐. Книжная полка
# Создайте класс:
# BookShelf
# Внутри хранится список названий книг.
# Реализуйте:
# __len__()
# __str__()
# __add__()
# `len(shelf)` возвращает количество книг.
# `print(shelf)` выводит книги по одной строке.
# При сложении двух полок должна создаваться новая полка с книгами обеих исходных полок.

class BookShelf:
    def __init__(self, book_list):
        self.book_list = book_list

    def __len__(self):
        return len(self.book_list)

    def __add__(self, other):
        if isinstance(other, BookShelf):
            new_book_list = [*self.book_list, *other.book_list]
            return BookShelf(new_book_list)

    def __str__(self):
        return "\n".join(str(item) for item in self.book_list)


shelf1 = BookShelf(["1984", "Дюна"])
shelf2 = BookShelf(["Солярис", "Марсианин"])

shelf3 = shelf1 + shelf2

print(shelf3)
print("Книг:", len(shelf3))
