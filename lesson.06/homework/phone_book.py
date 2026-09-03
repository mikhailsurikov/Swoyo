# Проект: Телефонный справочник. Часть 3
# Перепишите телефонный справочник из прошлого домашнего задания с использованием ООП.
# Сильно усложнять программу не нужно.
# ## Класс Contact
# Создайте класс:Contact
# Он хранит:name phone
# Добавьте метод:show_info()
# ## Класс PhoneBook
# Создайте класс:PhoneBook
# Внутри него хранится список объектов `Contact`:self.contacts = []
# Перенесите действия справочника в методы:
# add_contact()
# show_contacts()
# find_contact()
# update_contact()
# delete_contact()
# Меню остаётся прежним:
# 1. Добавить контакт
# 2. Показать все контакты
# 3. Найти контакт
# 4. Изменить контакт
# 5. Удалить контакт
# 6. Выйти
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def show_info(self):
        print(f"{self.name:<10} | {self.phone}")
        print("-" * 10 + "-+-" + "-" * 10)

    def set_name(self, name):
        self.name = name

    def set_phone(self, phone):
        self.phone = phone


class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        self.contacts.append(Contact(name, phone))
        print(f"Новый контакт {name} {phone} успешно добавлен")

    def show_contacts(self):
        if self.contacts:
            print("Список всех контактов: ")
            print(f"{'Имя':<10} | {'Телефон':<10}")
            print("-" * 10 + "-+-" + "-" * 10)
            for contact in self.contacts:
                contact.show_info()
        else:
            print("Список контактов пуст")

    def find_contact(self, name):
        for contact in self.contacts:
            if contact.name == name.capitalize():
                print(f"Найден контакт:")
                contact.show_info()
                return
        else:
            print(f'Контакт {name} не найден.')

    def update_contact(self, name):
        for contact in self.contacts:
            if contact.name == name.capitalize():
                new_name = input('Введите новое имя: \n')
                new_phone = input('Введите новый телефон: \n')
                contact.set_name(new_name)
                contact.set_phone(new_phone)
                print('Контакт изменён.')
                return
        else:
            print(f'Контакт {name} не найден.')

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name.capitalize():
                self.contacts.remove(contact)
                print(f'Контакт {name} удален.')
                return
        else:
            print(f'Контакт {name} не найден.')

    def print_actions(self):
        print("Доступные действия:")
        print("1. Добавить контакт")
        print("2. Показать все контакты")
        print("3. Найти контакт")
        print("4. Изменить контакт")
        print("5. Удалить контакт")
        print("6. Выйти")


def phone_book():
    print("Вы запустили телефонный справочник")
    phone_book = PhoneBook()
    phone_book.print_actions()
    action = input()
    while action != '6':
        if action == "1":
            print("Введите имя контакта и номер телефона(в формате +7...) через пробел: ")
            data = input()
            if not data.count(" "):
                print("Вы ввели данные некорректно")
                break
            name, phone = data.split(" ")
            if not name.isalpha() and phone[0] == "+" and phone[1:].isdigit():
                print("Вы ввели некорректные данные")
                break
            phone_book.add_contact(name.capitalize(), phone)
        elif action == '2':
            phone_book.show_contacts()
        elif action == '3':
            name = input('Введите имя контакта для поиска\n')
            phone_book.find_contact(name)
        elif action == '4':
            name = input('Введите имя контакта для изменения:\n')
            phone_book.update_contact(name)
        elif action == '5':
            name = input('Введите имя контакта для удаления:\n')
            phone_book.delete_contact(name)
        else:
            break
        phone_book.print_actions()
        action = input()
    print("Программа завершена")


if __name__ == "__main__":
    phone_book()
