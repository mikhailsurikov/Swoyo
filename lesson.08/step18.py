def add(a,b):
    if b == 0:
        raise ZeroDivisionError("Нельзя делить на ноль. Иди в школу")
    return a / b


print(add(3, 0))