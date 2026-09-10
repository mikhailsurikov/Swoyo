def get_int(text):
    while True:
        data = input(text)

        try:
            num = int(data)
            res = 100 / num
            break
        except ValueError as e:
            print(f'Ошибка ввода {e}')
            print("Введите еще раз" )
        except ZeroDivisionError:
            res = float('inf')
            break

    return num, res


if __name__ == '__main__':
    number = get_int("Введите целое число: ")
    print(number)