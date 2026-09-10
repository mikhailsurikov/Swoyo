class PhoneBookError(Exception):
    pass


class ContactNotFoundError(PhoneBookError):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Контакт {self.value} не найден"


class DuplicatePhoneBookError(PhoneBookError):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Контакт с именем {self.value} уже существует"
