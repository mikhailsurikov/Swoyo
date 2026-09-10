# Задание 7 ⭐. Бронирование места
# Создайте собственную иерархию исключений:
# BookingError
# InvalidSeatError
# SeatOccupiedError
# `BookingError` наследуется от `Exception`.
# Остальные исключения наследуются от `BookingError`.
# Напишите функцию:
# book_seat(seats, seat_number)
# `seats` — список занятых мест:
# seats = [2, 5, 8]
# В зале есть места от `1` до `10`.
# Функция должна:
# * вызвать `InvalidSeatError`, если такого места не существует;
# * вызвать `SeatOccupiedError`, если место уже занято;
# * добавить место в список, если бронирование возможно.

class BookingError(Exception):
    pass


class InvalidSeatError(BookingError):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Такого места {self.value} не существует"


class SeatOccupiedError(BookingError):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Место {self.value} уже занято "


def book_seat(seats, seat_number):
    if seat_number not in range(1, 11):
        raise InvalidSeatError(seat_number)
    elif seat_number in seats:
        raise SeatOccupiedError(seat_number)
    else:
        return f'Место {seat_number} забронировано'


seats = [2, 5, 8]

try:
    print(book_seat(seats, 7))
    print(book_seat(seats, 5))
except BookingError as error:
    print(error)
