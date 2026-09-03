# Задание 8 ⭐. Система бронирования мест
# Создайте класс:
# CinemaHall
# При создании передавайте количество мест.
# Количество свободных мест храните в приватном атрибуте:
# __free_seats
# Добавьте методы:
# book(count)
# cancel(count)
# get_free_seats()
# ### Правила
# `book(count)`:
# * уменьшает количество свободных мест;
# * нельзя забронировать больше мест, чем доступно;
# * нельзя передавать отрицательное количество.
# `cancel(count)`:
# * возвращает места;
# * количество свободных мест не должно становиться больше первоначального количества мест.

class CinemaHall:
    def __init__(self, seats):
        self.__free_seats = seats
        self.all_seats = seats

    def book(self, count):
        if count < 0:
            print("Введено некорректное значение")
        elif self.__free_seats - count < 0:
            print(f"Вы не можете забронировать {count} мест. Доступно для брони {self.__free_seats} мест")
        else:
            self.__free_seats -= count
            print(f"Успешно забронированных мест: {count}")

    def cancel(self, count):
        if count < 0:
            print("Введено некорректное значение")
        elif self.__free_seats + count > self.all_seats:
            print(f"Вы не можете вернуть {count} мест. Только {self.all_seats - self.__free_seats} мест")
        else:
            self.__free_seats += count
            print(f"Успешно возвращено мест: {count}")

    def get_free_seats(self):
        return self.__free_seats


hall = CinemaHall(100)

hall.book(20)
hall.book(30)
print(hall.get_free_seats())
hall.cancel(10)
print(hall.get_free_seats())
hall.book(60)
print(hall.get_free_seats())
hall.book(1)
print(hall.get_free_seats())
hall.cancel(99)
print(hall.get_free_seats())
hall.cancel(2)
