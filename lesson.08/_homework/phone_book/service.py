from .exceptions import *


class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        if contact.get_name() in [i.get_name() for i in self.contacts]:
            raise DuplicatePhoneBookError(contact.get_name())
        self.contacts.append(contact)
        print(f"Новый контакт {contact.get_name()} {contact.get_phone()} успешно добавлен")

    def show_contacts(self):
        return [contact for contact in self.contacts]

    def find_contact(self, name):
        for contact in self.contacts:
            if contact.get_name() == name.capitalize():
                print(f"Найден контакт: {contact}")
                return
        else:
            raise ContactNotFoundError(name)

    def update_contact(self, name):
        for contact in self.contacts:
            if contact.get_name() == name.capitalize():
                new_name = input('Введите новое имя: \n')
                new_phone = input('Введите новый телефон: \n')
                contact.set_name(new_name.capitalize())
                contact.set_phone(new_phone)
                print('Контакт изменён.')
                return
        else:
            raise ContactNotFoundError(name)

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.get_name() == name.capitalize():
                self.contacts.remove(contact)
                print(f'Контакт {name} удален.')
                return
        else:
            raise ContactNotFoundError(name)

    def print_actions(self):
        print("Доступные действия:")
        print("1. Добавить личный контакт")
        print("2. Добавить рабочий контакт")
        print("3. Показать все контакты")
        print("4. Найти контакт")
        print("5. Изменить контакт")
        print("6. Удалить контакт")
        print("7. Выйти")

    def __str__(self):
        if self.contacts:
            print("Список всех контактов: ")
            print(f"{'Имя':<10} | {'Телефон':<10}| {'Категория/Работа':<10} ")
            print(f'{"-" * 10} -+-{"-" * 10}')
            return f'\n{"-" * 10} -+-{"-" * 10}\n'.join(str(item) for item in self.contacts)
        else:
            return "Список контактов пуст"

    def __len__(self):
        return len(self.contacts)
