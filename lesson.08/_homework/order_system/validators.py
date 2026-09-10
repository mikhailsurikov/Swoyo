### `validators.py`
# Реализуйте:
# validate_price(price)
# validate_quantity(quantity)
# validate_discount(discount)
# Правила:
# * цена должна быть больше `0`;
# * количество должно быть целым числом и больше `0`;
# * скидка должна быть от `0` до `50`.
# При ошибках вызывайте соответствующие собственные исключения.
from .exceptions import *


def validate_price(price):
    if price < 0:
        raise InvalidPriceError(price)
    else:
        return price


def validate_quantity(quantity):
    if not isinstance(quantity, int):
        raise InvalidQuantityError(quantity)
    elif not not quantity < 0:
        raise InvalidQuantityError(quantity)
    else:
        return quantity


def validate_discount(discount):
    if not 0 < discount < 51:
        raise InvalidDiscountError(discount)
    else:
        return discount


if __name__ == '__main__':
    # validate_price(-1)
    # validate_quantity("abc")
    validate_quantity(-1)
    validate_discount(51)
