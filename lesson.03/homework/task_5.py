## Задание 5. Поиск и подсчёт слов
# Определите:
#
# 1. есть ли в строке слово `"python"`;
# 2. сколько раз оно встречается.

text = "python java python go python javascript"
if "python" in text:
    print("Слово найдено")
    print(f"Количество: {text.count('python')}")
else:
    print("Слово не найдено")
