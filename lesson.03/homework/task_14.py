# Задание 14 ⭐. Самый частый символ
# Найдите символ, который встречается в строке чаще всего.
# Если несколько символов встречаются одинаковое максимальное количество раз, достаточно вывести первый найденный.

text = "programming"
letters = {}
for letter in text:
    letters[letter] = text.count(letter)
max_count = max(letters.values())
max_letter = text[0]
for letter in letters:
    if letters[letter] == max_count:
        max_letter = letter
        break
print(
    f'Самый частый символ: {max_letter}\nКоличество: {max_count}')
