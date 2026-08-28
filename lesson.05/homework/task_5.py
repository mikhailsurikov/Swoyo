# Задание 5. Уникальные длины слов
# С помощью **set comprehension** получите множество длин всех слов, которые содержат больше `4` символов.

words = [
    "python",
    "java",
    "django",
    "go",
    "javascript",
    "flask",
    "fastapi"
]
data = {len(word) for word in words if len(word) > 4}
print(data)
