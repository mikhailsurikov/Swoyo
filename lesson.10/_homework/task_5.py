# Задание 5. Настройки программы в JSON
# Дан словарь:
# settings = {
#     "theme": "dark",
#     "language": "ru",
#     "notifications": True
# }
# Сохраните его в файл:
# settings.json
# После этого:
# 1. прочитайте данные из файла;
# 2. измените `"theme"` на `"light"`;
# 3. добавьте `"font_size": 16`;
# 4. снова сохраните данные в файл.
import json

settings = {
    "theme": "dark",
    "language": "ru",
    "notifications": True
}

filename = 'settings.json'

with open(filename, mode='w', encoding='utf-8') as file:
    json.dump(settings, file, ensure_ascii=False, indent=2)

with open(filename, mode='r', encoding='utf-8') as file:
    data = json.load(file)

data["theme"] = "light"
data["font_size"] = 16

with open(filename, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open(filename, mode='r', encoding='utf-8') as file:
    print(file.read())
