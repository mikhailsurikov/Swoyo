# Задание 12 ⭐. Анализ строки
# Напишите функцию:
# Функция должна подсчитать:
# * количество букв;
# * количество цифр;
# * количество остальных символов.
# Результат необходимо вернуть в виде словаря:

def analyze_text(text):
    letters = len([symbol for symbol in text if symbol.isalpha()])
    digits = len([symbol for symbol in text if symbol.isdigit()])
    other = len([symbol for symbol in text if not symbol.isalnum()])
    return {"letters": letters, "digits": digits, "others": other}


print(analyze_text("Python 2026!"))
