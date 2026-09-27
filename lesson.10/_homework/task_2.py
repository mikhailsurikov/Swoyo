# Задание 2. Список покупок
# Дан список:
# products = [
#     "Хлеб",
#     "Молоко",
#     "Сыр",
#     "Яблоки"
# ]
# Запишите его в файл:
# shopping.txt
# Каждый товар должен находиться на отдельной строке.
# После этого снова откройте файл и выведите его содержимое.

products = [
    "Хлеб",
    "Молоко",
    "Сыр",
    "Яблоки"
]
with open('shopping.txt', mode='w', encoding='utf-8') as file:
    file.writelines(prod + '\n' for prod in products)

with open('shopping.txt', encoding='utf-8') as file:
    print(file.read())
