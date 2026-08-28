# Задание 8. Простое число
# Напишите функцию:
# Функция должна определить, является ли число простым.
# Простое число:
# * больше `1`;
# * делится без остатка только на `1` и само себя.
# Функция возвращает `True` или `False`.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


print(is_prime(7))
print(is_prime(13))
print(is_prime(12))
print(is_prime(1))
print(is_prime(2))
