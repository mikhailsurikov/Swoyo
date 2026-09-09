class UserBaseException(Exception):
    pass


class UserAgeError(UserBaseException):
    pass


class UserNameError(UserBaseException):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f"Имя должно быть другое {self.value}"



def add(a,b):
    if b == 0:
        raise UserNameError("Текст при ошибке !")
    return a / b


print(add(3, 0))