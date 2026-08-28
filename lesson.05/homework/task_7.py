# Задание 7. Слова и их длина
# С помощью **dict comprehension** создайте словарь:
# * ключ - слово;
# * значение - длина слова.
# В словарь должны попасть только слова длиной не менее `5` символов.

words = ["python", "java", "go", "javascript", "django", "sql"]
data = {word: len(word) for word in words if len(word) > 4}
print(data)
