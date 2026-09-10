# Задание 8 ⭐. Пакет обработки заказов
# Создайте пакет:
# order_system/
#     __init__.py
#     exceptions.py
#     validators.py
#     calculator.py
# main.py
### `main.py`
# Запросите:
# * цену;
# * количество;
# * скидку.
# Обработайте:
# * `ValueError` при преобразовании введённых значений;
# * `OrderError` и его дочерние исключения.
# Если ошибок нет, выведите результат в `else`.
# В `finally` всегда выводите:
# Обработка заказа завершена
from order_system import calculate_total, OrderError


def create_order():
    try:
        price = int(input("Введите цену: "))
        quantity = int(input("Введите количество: "))
        discount = int(input("Введите скидку: "))
        try:
            print(
                f"Цена: {price}\nКоличество: {quantity}\nСкидка: {discount}%\nИтого: "
                f"{calculate_total(price, quantity, discount)}")
        except OrderError as e:
            print(e)
    except ValueError:
        print("Значение должно быть числом")
    finally:
        print('Обработка заказа завершена')


if __name__ == '__main__':
    create_order()
