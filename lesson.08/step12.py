def get_int(text):
    while True:
        data = input(text)

        try:
            num = int(data)
            break
        except ValueError as e:
            print(f'Ошибка ввода {e}')
            print("Введите еще раз" )
    return num


if __name__ == '__main__':
    number = get_int("Введите целое число: ")
    print(number)