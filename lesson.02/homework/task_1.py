# Задание 1. Изменение кортежа через список
# Преобразуйте его в список, добавьте число 6, а затем преобразуйте обратно в кортеж.

numbers = (1, 2, 3, 4, 5)
new_numbers = list(numbers)
new_numbers.append(6)
numbers = tuple(new_numbers)
print(numbers)
