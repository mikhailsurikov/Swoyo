# Задание 12 ⭐. Многочлен
# Создайте класс:
# Polynomial
# Коэффициенты передаются списком.
# Например:
# Polynomial([2, 3, 1])
# означает: 2x² + 3x + 1
# Для упрощения считаем, что складываемые многочлены имеют одинаковое количество коэффициентов.
# Реализуйте: __str__(), __add__(),__call__()
# ### `__str__()`
# Должен возвращать многочлен в читаемом виде: 2x^2 + 3x + 1
# Для упрощения можно:
# * не убирать коэффициенты, равные `0`;
# * не делать отдельное красивое форматирование отрицательных коэффициентов.
# Например допустимо: 2x^2 + 0x + 1 and  2x^2 + -3x + 1
# ### `__add__()`
# Позволяет складывать многочлены. p1 = Polynomial([2, 3, 1]) p2 = Polynomial([1, 0, 4]) p3 = p1 + p2
# Получаем:
# 3x^2 + 3x + 5
# ### `__call__()`
# Объект должен работать как функция.
# p1(2)
# для: 2x² + 3x + 1
# означает: 2 * 2² + 3 * 2 + 1

class Polynomial:
    def __init__(self, coefficient):
        self.coefficient = coefficient
        self.a, self.b, self.c = self.coefficient

    def __str__(self):
        return f'{self.a}x² + {self.b}x + {self.c}'

    def __add__(self, other):
        return Polynomial([self.a + other.a, self.b + other.b, self.c + other.c])

    def __call__(self, data):
        return 2 * data ** 2 + 3 * data + 1


p1 = Polynomial([2, 3, 1])
p2 = Polynomial([1, 0, 4])

p3 = p1 + p2

print(p1)
print(p3)
print(p1(2))
