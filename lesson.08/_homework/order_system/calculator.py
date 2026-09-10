### `calculator.py`
# Реализуйте:
# calculate_total(price, quantity, discount=0)
# Алгоритм:
# 1. Посчитать стоимость:
# price * quantity
# 2. Вычесть указанный процент скидки.
# Например:
# 1000 * 3 = 3000
# скидка 10% = 300
# итого = 2700
# Перед расчётом используйте функции из `validators.py`.
from .validators import *


def calculate_total(price, quantity, discount):
    return round((validate_price(price) * validate_quantity(quantity)) * (1 - validate_discount(discount) / 100), 2)


if __name__ == '__main__':
    print(calculate_total(1000, 3, 10))
