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
    def __init__(self, name: str, phone: str):
        self.__name = name
        self.__phone = phone

    def set_name(self, name):
        self.__name = name

    def set_phone(self, phone):
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    def __str__(self):
        return f'{self.get_name():<10} | {self.get_phone()}'


class PersonalContact(Contact):
    def __init__(self, relation: str, *args):
        self.__relation = relation
        super().__init__(*args)

    def __str__(self):
        return f'{self.get_name():<10} | {self.get_phone():<10} | {self.__relation}'

    def set_relation(self, relation):
        self.__relation = relation


class WorkContact(Contact):
    def __init__(self, company: str, *args):
        self.__company = company
        super().__init__(*args)

    def __str__(self):
        return f'{self.get_name():<10} | {self.get_phone():<10} | {self.__company}'

    def set_company(self, company):
        self.__company = company


class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
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
            print(f'Контакт {name} не найден.')

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
            print(f'Контакт {name} не найден.')

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.get_name() == name.capitalize():
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


def phone_book():
    print("Вы запустили телефонный справочник")
    phone_book = PhoneBook()
    phone_book.print_actions()
    action = input()
    while action != '6':
        if action == "1":
            print("Введите имя контакта и номер телефона (категорию или работу) через пробел: ")
            data = input()
            if not data.count(" "):
                print("Вы ввели данные некорректно")
                break
            if data.count(" ") == 1:
                name, phone = data.split(" ")
                if not name.isalpha() and phone[0] == "+" and phone[1:].isdigit():
                    print("Вы ввели некорректные данные")
                    break
                phone_book.add_contact(Contact(name.capitalize(), phone))
            if data.count(" ") == 2:
                name, phone, data = data.split(" ")
                if data in ("друг", "родственник", "знакомый"):
                    phone_book.add_contact(PersonalContact(data, name.capitalize(), phone))
                else:
                    phone_book.add_contact(WorkContact(data, name.capitalize(), phone))
        elif action == '2':
            print(phone_book)
            print("Всего контактов:", len(phone_book))
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
            print("Вы ввели команду некорректно")
        phone_book.print_actions()
        action = input()
    print("Программа завершена")


if __name__ == "__main__":
    phone_book()
