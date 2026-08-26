# Проект: Телефонный справочник. Часть 2
# Доработайте телефонный справочник из предыдущего домашнего задания.
# Теперь каждый контакт должен храниться в виде словаря:
# {
#     "name": "Анна",
#     "phone": "12345"
# }
# Все контакты хранятся в списке:
#
# contacts = [
#     {"name": "Анна", "phone": "12345"},
#     {"name": "Иван", "phone": "67890"}
# ]
#
# ## Требования
# Программа должна работать в цикле и показывать меню:
#
# 1. Добавить контакт
# 2. Показать все контакты
# 3. Найти контакт
# 4. Изменить контакт
# 5. Удалить контакт
# 6. Выйти
# Каждое действие необходимо вынести в отдельную функцию.

def phone_book():
    contacts = []
    print("Вы запустили телефонный справочник")

    def add_contact(name, phone):
        contacts.append({"name": name, "phone": phone})
        print(f"Новый контакт {name} {phone} успешно добавлен")

    def show_contacts():
        if contacts:
            print("Список всех контактов: ")
            print(f"{'Имя':<10} | {'Телефон':<10}")
            print("-" * 10 + "-+-" + "-" * 10)
            for contact in contacts:
                print(f"{contact.get('name'):<10} | {contact.get('phone')}")
                print("-" * 10 + "-+-" + "-" * 10)
        else:

            print("Список контактов пуст")

    def find_contact(name):
        for contact in contacts:
            if contact.get('name') == name.capitalize():
                print(f"Найден контакт:\n{contact.get('name'):<10} | {contact.get('phone'):<10}")
                return
        else:
            print(f'Контакт {name} не найден.')

    def update_contact(name):
        for contact in contacts:
            if contact.get("name") == name.capitalize():
                new_name = input('Введите новое имя: \n')
                new_phone = input('Введите новый телефон: \n')
                contact.update({"name": new_name.capitalize(), "phone": new_phone})
                print('Контакт изменён.')
                return
        else:
            print(f'Контакт {name} не найден.')

    def delete_contact(name):
        for contact in contacts:
            if contact.get("name") == name.capitalize():
                contacts.remove(contact)
                print(f'Контакт {name} удален.')
                return
        else:
            print(f'Контакт {name} не найден.')

    print("Доступные действия:")
    print("1. Добавить контакт")
    print("2. Показать все контакты")
    print("3. Найти контакт")
    print("4. Изменить контакт")
    print("5. Удалить контакт")
    print("6. Выйти")
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
            add_contact(name.capitalize(), phone)
        elif action == '2':
            show_contacts()
        elif action == '3':
            name = input('Введите имя контакта для поиска\n')
            find_contact(name)
        elif action == '4':
            name = input('Введите имя контакта для изменения:\n')
            update_contact(name)
        elif action == '5':
            name = input('Введите имя контакта для удаления:\n')
            delete_contact(name)
        else:
            break
        print("Доступные действия:")
        print("1. Добавить контакт")
        print("2. Показать все контакты")
        print("3. Найти контакт")
        print("4. Изменить контакт")
        print("5. Удалить контакт")
        print("6. Выйти")
        action = input()
    print("Программа завершена")


if __name__ == "__main__":
    phone_book()
