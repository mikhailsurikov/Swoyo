# Задание 4. Безопасный ввод числа
# Напишите функцию:
# get_positive_number()
# Она должна запрашивать положительное целое число.
# Если пользователь вводит значение, которое нельзя преобразовать в `int`, обработайте `ValueError` и попросите повторить ввод.
# Если число равно `0` или меньше `0`, также запросите значение ещё раз.

def get_positive_number():
    while True:
        data = input("Введите число: ")
        try:
            number = int(data)
            if number <= 0:
                print(f'Число должно быть больше 0')
                continue
            else:
                print(f'Успешно, возвращаю {number}')
                return number
        except ValueError:
            print(f'Необходимо ввести целое число')
            continue


if __name__ == '__main__':
    get_positive_number()
