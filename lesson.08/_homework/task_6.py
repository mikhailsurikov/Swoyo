# Задание 6. Проверка данных через `raise`
# Напишите функцию:
# create_user(name, age)
# Правила для имени:
# * значение должно быть строкой;
# * строка не должна быть пустой;
# * имя должно содержать только буквы.
# Правила для возраста:
# * значение должно быть целым числом;
# * возраст должен быть от `1` до `119`.
# Используйте:
# * `TypeError` — если передан неправильный тип;
# * `ValueError` — если тип правильный, но значение некорректно.
# Исключения нужно создавать самостоятельно через `raise`.
# Если данные корректны, функция возвращает:
# {
#     "name": "Анна",
#     "age": 25
# }
def create_user(name, age):
    if not isinstance(name, str):
        raise TypeError("значение должно быть строкой")
    if not name:
        raise ValueError("строка не должна быть пустой")
    if not name.isalpha():
        raise ValueError("имя должно содержать только буквы")
    if not isinstance(age, int):
        raise TypeError("значение должно быть целым числом")
    if not 0 < age < 120:
        raise ValueError("возраст должен быть от 1 до 119")
    return {
        "name": name,
        "age": age}


try:
    user = create_user("Анна", 25)
    print(user)
except (ValueError, TypeError) as error:
    print(error)

try:
    user = create_user("", 25)
    print(user)
except (ValueError, TypeError) as error:
    print(error)

try:
    user = create_user(123, 25)
    print(user)
except (ValueError, TypeError) as error:
    print(error)

try:
    user = create_user("Анна", 0)
    print(user)
except (ValueError, TypeError) as error:
    print(error)

try:
    user = create_user("Анна", "12")
    print(user)
except (ValueError, TypeError) as error:
    print(error)
