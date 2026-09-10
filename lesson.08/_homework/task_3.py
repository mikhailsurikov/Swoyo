# Задание 3. Собственный пакет
# Создайте пакет:
# text_tools/
#     __init__.py
#     names.py
#     phones.py
# В `names.py` реализуйте:
# format_name(name)
# Функция должна убрать пробелы по краям и привести имя к нормальному виду:
# "   иВАН   " → "Иван"
# В `phones.py` реализуйте:
# hide_phone(phone)
# Пример:
# "+79991234567" → "+7999***4567"
# Настройте `__init__.py` и `__all__`, чтобы функции можно было импортировать так:
# from text_tools import format_name, hide_phone
from text_tools import format_name, hide_phone

print(format_name("   аННА   "))
print(hide_phone("+79991234567"))
