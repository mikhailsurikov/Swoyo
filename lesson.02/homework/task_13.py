# Задание 13 ⭐. Лучший студент
# Для каждого студента вычислите среднюю оценку.
# После этого найдите студента с самой высокой средней оценкой.
# Если одинаковый лучший результат получили несколько студентов, выведите их всех.

grades = {
    "Анна": (5, 4, 5, 5),
    "Иван": (4, 4, 3, 5),
    "Олег": (3, 4, 3, 3),
    "Мария": (5, 5, 5, 4)
}
average_grades = {}
for k, v in grades.items():
    average_grades.update({k: sum(v) / len(v)})
max_avg_grade = max(average_grades.values())
print(f"Лучшая средняя оценка: {max_avg_grade}")
best_students = []
for k, v in average_grades.items():
    if v == max_avg_grade:
        best_students.append(k)
if len(best_students) == 1:
    print(f"Лучший студент: {best_students[0]}")
else:
    print(f"Лучшие студенты: {', '.join(best_students)}")
