# Задание 10 ⭐. Генератор простых чисел
# Напишите функцию-генератор:
# Она должна генерировать первые `count` простых чисел, начиная с `2`.
# Простым считается число, которое:
# * больше `1`;
# * делится без остатка только на `1` и само себя.

def prime_numbers(count):
    if count <= 0:
        return
    yield 2
    if count == 1:
        return
    found = [2]
    n = 3
    while len(found) < count:
        is_prime = True
        for p in found:
            if p * p > n:
                break
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            found.append(n)
            yield n
        n += 2


for number in prime_numbers(10):
    print(number)

# for number in prime_numbers(10):
#     print(number)
#
#
# ### Результат
#
#
# 2
# 3
# 5
# 7
# 11
# 13
# 17
# 19
# 23
# 29
