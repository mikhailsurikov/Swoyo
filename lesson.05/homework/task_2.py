# Задание 2. Отбор слов
# С помощью **list comprehension** создайте новый список.
# В него должны попасть только непустые строки длиной не менее `4` символов.

words = ["python", "", "java", "django", "", "go", "javascript"]
new_words = [word for word in words if len(word) > 3]
print(new_words)
