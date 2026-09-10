from phone_book import (PhoneBook, PersonalContact, WorkContact, PhoneBookError)


def phone_book_func():
    print("Вы запустили телефонный справочник")
    phone_book = PhoneBook()
    phone_book.print_actions()
    action = input()
    while action != '7':
        if action == "1":
            print("Введите имя контакта и номер телефона и категорию через пробел: ")
            name, phone, category = input().split(" ")
            if not name.isalpha() and phone[0] == "+" and phone[1:].isdigit():
                raise ValueError("Вы ввели некорректные данные")
            phone_book.add_contact(PersonalContact(category, name.capitalize(), phone))
        elif action == "2":
            print("Введите имя контакта и номер телефона и работу через пробел: ")
            name, phone, work = input().split(" ")
            if not name.isalpha() and phone[0] == "+" and phone[1:].isdigit():
                raise ValueError("Вы ввели некорректные данные")
            try:
                phone_book.add_contact(WorkContact(work, name.capitalize(), phone))
            except PhoneBookError as error:
                print(error)
        elif action == '3':
            print(phone_book)
            print("Всего контактов:", len(phone_book))
        elif action == '4':
            name = input('Введите имя контакта для поиска\n')
            try:
                phone_book.find_contact(name)
            except PhoneBookError as error:
                print(error)
        elif action == '5':
            name = input('Введите имя контакта для изменения:\n')
            try:
                phone_book.update_contact(name)
            except PhoneBookError as error:
                print(error)
        elif action == '6':
            name = input('Введите имя контакта для удаления:\n')
            try:
                phone_book.delete_contact(name)
            except PhoneBookError as error:
                print(error)
        else:
            raise ValueError("Вы ввели команду некорректно")
        phone_book.print_actions()
        action = input()
    print("Программа завершена")


if __name__ == "__main__":
    phone_book_func()
