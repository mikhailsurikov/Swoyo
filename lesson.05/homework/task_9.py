# Задание 9 ⭐. Генератор накопительной суммы
# Напишите функцию-генератор:
# Она принимает список чисел и после каждого элемента возвращает текущую сумму всех просмотренных чисел.

def sum_generator(numbers):
    res = 0
    for i in numbers:
        res += i
        yield res


numbers = [5, 10, 3, 7]
print(*sum_generator(numbers))
