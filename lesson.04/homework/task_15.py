# Задание 15 ⭐. Лучший студент
# Дан словарь:
# grades = {
#     "Анна": (5, 4, 5, 5),
#     "Иван": (4, 4, 3, 5),
#     "Олег": (3, 4, 3, 3),
#     "Мария": (5, 5, 5, 5)
# }
# Напишите функцию:
# Функция должна:
# 1. вычислить среднюю оценку каждого студента;
# 2. найти студента с самой высокой средней оценкой;
# 3. вернуть его имя и среднюю оценку.

def find_best_student(grades):
    avg_grades = {}
    for k, v in grades.items():
        avg_grades[k] = sum(v) / len(v)
    best_student = ""
    best_grade = 0
    for k, v in avg_grades.items():
        if v > best_grade:
            best_student = k
            best_grade = v
    return f'Лучший студент: {best_student}\nСредняя оценка: {best_grade}'


grades = {
    "Анна": (5, 4, 5, 5),
    "Иван": (4, 4, 3, 5),
    "Олег": (3, 4, 3, 3),
    "Мария": (5, 5, 5, 5)
}
print(find_best_student(grades))
