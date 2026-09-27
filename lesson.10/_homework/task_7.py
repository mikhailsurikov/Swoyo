# Задание 7 ⭐. Конвертация CSV в JSON
# Дан файл:
# students.csv
# Анна,5,4,5
# Иван,4,3,4
# Мария,5,5,5
# Олег,3,4,3
# Каждая строка содержит:
# имя, оценка1, оценка2, оценка3
# Считайте, что у каждого студента указаны ровно три оценки.
# Прочитайте CSV-файл и сформируйте список словарей:
# [
#     {
#         "name": "Анна",
#         "grades": [5, 4, 5],
#         "average": 4.67
#     },
#     ...
# ]
# Среднюю оценку округлите до двух знаков.
# Сохраните результат в:
# students.json
# Дополнительно найдите студента с самой высокой средней оценкой.
import json
import csv

students_data = []
with open('students.csv', 'r', newline='', encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        students_data.append(
            {"name": row[0], "grades": row[1:], "average": round(sum(map(int, row[1:])) / len(row[1:]), 2)})

with open('students.json', "w", encoding="utf-8") as f:
    json.dump(students_data, f, ensure_ascii=False, indent=2)

with open('students.json', "r", encoding="utf-8") as f:
    print(f.read())
best_student = max(students_data, key=lambda d: d["average"])
print(f"Лучший студент: {best_student['name']}\nСредняя оценка: {best_student['average']}")
