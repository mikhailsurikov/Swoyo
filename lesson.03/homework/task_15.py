# Задание 15 ⭐. Анализ строки
# Попросите пользователя ввести строку.
# Посчитайте отдельно:
# * количество букв;
# * количество цифр;
# * количество остальных символов, включая пробелы и знаки препинания.

text = input('Введите текст: ')
letters = len([symbol for symbol in text if symbol.isalpha()])
digits = len([symbol for symbol in text if symbol.isdigit()])
other = len([symbol for symbol in text if not symbol.isalnum()])
print(f'Букв: {letters}\nЦифр: {digits}\nДругих символов: {other}')
