# Задание 10 ⭐. Двумерный вектор
# Создайте класс:
# Vector2D
# Он хранит:
# x
# y
# Реализуйте:
# __str__()
# __add__()
# __sub__()
# __eq__()
# __call__()
# ### Сложение
# (x1, y1) + (x2, y2)
# =
# (x1 + x2, y1 + y2)
# ### Вычитание
# (x1, y1) - (x2, y2)
# =
# (x1 - x2, y1 - y2)
# Два вектора равны, если совпадают обе координаты.
# При вызове объекта:
# vector(3)
# должен возвращаться новый вектор, координаты которого умножены на `3`.

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __add__(self, other):
        return Vector2D((self.x + other.x), (self.y + other.y))

    def __sub__(self, other):
        return Vector2D((self.x - other.x), (self.y - other.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __call__(self, value):
        return f"({self.x * value}, {self.y * value})"


v1 = Vector2D(2, 3)
v2 = Vector2D(4, 1)

print(v1 + v2)
print(v1 - v2)
print(v1 == Vector2D(2, 3))
print(v1(3))
