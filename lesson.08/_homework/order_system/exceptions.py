class OrderError(Exception):
    pass


class InvalidPriceError(OrderError):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Цена должна быть больше 0"


class InvalidQuantityError(OrderError):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"количество должно быть целым числом и больше 0"


class InvalidDiscountError(OrderError):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Скидка должна быть от 0 до 50"
