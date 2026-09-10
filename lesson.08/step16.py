def get_int(text):
    data = input(text)

    try:
        num = int(data)
    except ValueError as e:
        print(f'Ошибка ввода {e}')
        num = 10000
    finally:
        print("Показываюсь всегда")
    return num


if __name__ == '__main__':
    number = get_int("Введите целое число: ")
    print(number)