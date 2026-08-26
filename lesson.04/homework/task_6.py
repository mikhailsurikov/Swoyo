# Задание 6. Проверка домена
# Напишите функцию:
# Функция должна возвращать `True`, если строка похожа на доменное имя.
# Допустимые окончания:
# .org
# .com
# .info
# Перед доменной зоной должно находиться не менее двух символов.

def is_domain(value):
    if len(value.split('.')[0]) > 1 and any([value.endswith(_) for _ in [".org", ".com", ".info"]]):
        return True
    else:
        return False


print(is_domain("mycats.com"))
print(is_domain("python.org"))
print(is_domain("ab.info"))
print(is_domain("1.com"))
print(is_domain("example.ru"))
