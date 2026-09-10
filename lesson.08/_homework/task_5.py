# Задание 5. Расчёт стоимости заказа
# Напишите функцию:
# calculate_order(price, quantity)
# Значения могут передаваться строками:
# calculate_order("125.5", "4")
# Внутри функции преобразуйте:
# * `price` в `float`;
# * `quantity` в `int`.
# Обработайте:
# * `ValueError` — значение невозможно преобразовать в число;
# * `TypeError` — передан неподходящий тип данных.
# Если ошибок нет, в блоке `else` верните стоимость заказа.
# В `finally` всегда выводите:
# Расчёт завершён

def calculate_order(price, quantity):
    try:
        result = float(price) * int(quantity)
    except ValueError:
        print('Значение невозможно преобразовать в число')
    except TypeError:
        print('Передан неподходящий тип данных')
    else:
        return result
    finally:
        print('Расчёт завершён')


print(calculate_order("125.5", "4"))
print(calculate_order("сто", "4"))
