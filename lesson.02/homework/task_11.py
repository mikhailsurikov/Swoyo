# Задание 11⭐. Частота появления слов
# Создайте словарь, в котором:
# * ключ - слово;
# * значение - количество его появлений в кортеже.

words = (
    "python",
    "java",
    "python",
    "go",
    "java",
    "python",
    "javascript",
    "go")
words_dict = {}
for word in words:
    words_dict.update({word: words.count(word)})
print(words_dict)
