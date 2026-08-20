# Задание 14 ⭐. Анализ трёх групп
# Даны три множества:
# Найдите:
# 1. студентов, которые посещают все три курса;
# 2. студентов, которые посещают хотя бы один курс;
# 3. студентов, которые посещают Python, но не посещают Django и Docker.

python_group = {"Анна", "Иван", "Мария", "Олег", "Алексей"}
django_group = {"Иван", "Мария", "Сергей", "Алексей"}
docker_group = {"Мария", "Алексей", "Павел", "Иван"}
print(f'Все три курса: {python_group & django_group & docker_group}')
print(f'Хотя бы один курс: {python_group | django_group | docker_group}')
print(f'Только Python: {python_group - django_group - docker_group}')
