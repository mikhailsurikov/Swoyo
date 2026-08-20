# Задание 6. Участники двух курсов

# Даны множества студентов:
# Выведите:
# * студентов, которые посещают оба курса;
# * студентов, которые посещают только Python.

python_students = {"Анна", "Иван", "Олег", "Мария"}
web_students = {"Иван", "Мария", "Алексей"}
print(f"Оба курса {web_students & python_students}")
print(f"Только Python {python_students - web_students}")
