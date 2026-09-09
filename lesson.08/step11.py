def get_int(text: str) -> int:
    data = input(text)
    num = int(data)
    return num


if __name__ == '__main__':
    number = get_int("Введите целое число: ")
    print(number)