# Задание 7. Максимальное число списка
# Напишите функцию:
# Функция принимает непустой список чисел и возвращает самое большое число.
# **Использовать встроенную функцию `max()` нельзя.**

def max_in_list(numbers):
    max_num = numbers[0]
    for number in numbers:
        if number > max_num:
            max_num = number
    return max_num


print(max_in_list([4, 12, 7, 3, 18, 5]))
print(max_in_list([-5, -2, -10, -1]))
