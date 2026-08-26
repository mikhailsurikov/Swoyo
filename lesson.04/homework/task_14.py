# Задание 14 ⭐. Рекурсивная сумма
# Напишите рекурсивную функцию:
# Она должна вычислять сумму всех чисел от `1` до `n`.

def sum_to_n(n):
    if n != 0:
        return n + sum_to_n(n - 1)
    else:
        return n


print(sum_to_n(5))
print(sum_to_n(10))
print(sum_to_n(1))
