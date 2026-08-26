# Задание 10. Сумма произвольного количества чисел
# Напишите функцию:
# Функция должна принимать любое количество чисел и возвращать их сумму.
# Если числа не переданы, функция должна вернуть `0`.

def sum_numbers(*args):
    data = 0
    for _ in args:
        data += _
    return data


print(sum_numbers(1, 2, 3))
print(sum_numbers(10, 20, 30, 40))
print(sum_numbers(5))
print(sum_numbers())
