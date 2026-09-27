# Задание 1. Статистика текстового файла
# Создайте файл:
# article.txt
# С содержимым:
# Python используется для веб-разработки.
# Python подходит для автоматизации.
# Изучать Python интересно.
# Напишите программу, которая с помощью `with`:
# 1. читает файл;
# 2. выводит количество строк;
# 3. выводит количество символов во всём тексте.
# Количество символов считайте вместе с пробелами и переносами строк.
# В примере после последней строки дополнительного переноса строки нет.

def file_statistics(file_name):
    """Функция считает количество строк и всех символов в файле"""
    with open(file_name, mode='r', encoding='utf-8') as file:
        line_count = 0
        symbol_count = 0
        for line in file.readlines():
            line_count += 1
            symbol_count += len(line)
        print(f'Строк: {line_count}\nСимволов: {symbol_count}')


if __name__ == '__main__':
    file_statistics('article.txt')
