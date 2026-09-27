from .exceptions import *
import random
import json
from pathlib import Path
from .contacts import PersonalContact, WorkContact


class PhoneBook:
    def __init__(self):
        self.contacts = []
        self.__path = Path('data/contacts.json')

    def add_contact(self, contact):
        if contact.get_name() in [i.get_name() for i in self.contacts]:
            raise DuplicateContactError(contact.get_name())
        self.contacts.append(contact)
        print(f"Новый контакт {contact.get_name()} {contact.get_phone()} успешно добавлен")
        self.save()

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
                self.save()
                return
        else:
            raise ContactNotFoundError(name)

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.get_name() == name.capitalize():
                self.contacts.remove(contact)
                print(f'Контакт {name} удален.')
                self.save()
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
        print("7. Показать случайный контакт")
        print("8. Выйти")

    def random_contact(self):
        if self.contacts:
            print(random.choice(self.contacts))
        else:
            raise ContactNotFoundError("")

    def save(self):
        """Метод сохраняет контакты в JSON."""
        if not self.__path.exists():
            self.__path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.__path, "w", encoding="utf-8") as file:
            json.dump([contact.to_dict() for contact in self.contacts], file, ensure_ascii=False, indent=2)

    def load(self):
        """Метод выгружает контакты из JSON файла."""
        if not self.__path.exists():
            return "Список контактов пуст"
        try:
            with open(self.__path, "r", encoding="utf-8") as file:
                data = json.load(file)
                p_contacts = [PersonalContact.from_dict(i) for i in data if i.get("type") == "personal"]
                w_contacts = [WorkContact.from_dict(i) for i in data if i.get("type") == "work"]
                self.contacts = [*p_contacts, *w_contacts]
        except json.JSONDecodeError:
            print("Не удалось загрузить контакты")

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
