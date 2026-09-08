from functools import total_ordering


# Задание 9 ⭐. Версии программы
# Создайте класс:
# Version
# Версия передаётся строкой:
# "2.5.10"
# Она состоит из:
# major.minor.patch
# Необходимо поддержать:
# ==
# !=
# <
# >
# <=
# >=
# Сравнение выполняется последовательно:
# 1. `major`;
# 2. `minor`;
# 3. `patch`.
# Используйте:
# __eq__()
# __lt__()
# Также реализуйте `__str__()`.
# Для упрощения считаем, что строка версии всегда корректная и содержит ровно три числа.

@total_ordering
class Version:
    def __init__(self, value: str):
        self.value = value
        self.major, self.minor, self.patch = map(int, self.value.split('.'))

    def __eq__(self, other):
        return self.major == other.major and self.minor == other.minor and self.patch == other.patch

    def __lt__(self, other):
        if self.major != other.major:
            return self.major < other.major
        elif self.minor != other.minor:
            return self.minor < other.minor
        elif self.patch != other.patch:
            return self.patch < other.patch
        else:
            return False

    def __str__(self):
        return self.value


v1 = Version("1.10.0")
v2 = Version("1.2.9")
v3 = Version("2.0.0")
v4 = Version("1.2.9")

print(v1 > v2)
print(v1 < v3)
print(v2 == v4)
print(v2 == v1)
print(v1)
