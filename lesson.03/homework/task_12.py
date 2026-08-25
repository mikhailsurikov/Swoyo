# Задание 12 ⭐. Подсчёт гласных
# Посчитайте количество русских гласных букв в строке.
# Учитывайте как строчные, так и заглавные буквы.

text = "Программирование на Python"
vowels = ['е', 'а', 'о', 'э', 'я', 'и', 'ю', 'у']
vowels_count = 0
for letter in vowels:
    vowels_count += text.lower().count(letter)
print(f'Количество гласных: {vowels_count}')
