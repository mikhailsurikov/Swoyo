from copy import deepcopy


# Задание 13 ⭐. Обновление данных пользователя через `**kwargs`
# Дан словарь:
# user = {
#     "name": "Анна",
#     "age": 25,
#     "city": "Москва"
# }
# Напишите функцию:
# Функция должна:
# 1. создать копию исходного словаря;
# 2. добавить или изменить в копии все данные, переданные через `**kwargs`;
# 3. вернуть новый словарь;
# 4. не изменять исходный словарь.
# При этом исходный словарь `user` должен остаться без изменений.


def update_user(user, **kwargs):
    new_user = deepcopy(user)
    new_user.update(kwargs)
    return new_user


user = {
    "name": "Анна",
    "age": 25,
    "city": "Москва"
}

result = update_user(
    user,
    age=26,
    city="Казань",
    profession="Developer"
)
print(result)
