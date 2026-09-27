# Задание 4. JSON-строка
# Дан словарь:
# user = {
#     "name": "Анна",
#     "age": 25,
#     "city": "Казань",
#     "active": True
# }
# С помощью `json.dumps()` преобразуйте словарь в JSON-строку.
# После этого с помощью `json.loads()` преобразуйте строку обратно в Python-объект.
# Выведите:
# * JSON-строку;
# * имя пользователя;
# * город.
# Русские символы должны сохраняться в читаемом виде.
import json

user = {
    "name": "Анна",
    "age": 25,
    "city": "Казань",
    "active": True
}
json_string = json.dumps(user)
print(json_string)
json_data = json.loads(json_string)
print(json_data.get("name"))
print(json_data.get("city"))
