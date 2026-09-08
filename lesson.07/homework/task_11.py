# Задание 11 ⭐. Цепочка обработки данных
# Создайте классы:
# BaseProcessor
# ValidationProcessor
# LoggingProcessor
# `BaseProcessor` содержит метод:
# process(data)
# который возвращает:
# Обработано: <данные>
# `ValidationProcessor` реализует `process()`:
# * если строка пустая, возвращает `"Нет данных"`;
# * иначе передаёт выполнение следующему классу через `super()`.
# `LoggingProcessor`:
# * выводит `"LOG: <данные>"`;
# * затем передаёт выполнение дальше через `super()`.
# Создайте класс:
# DataService
# с множественным наследованием:
# LoggingProcessor
# ValidationProcessor
# BaseProcessor

class BaseProcessor:

    def process(self, data):
        return f'Обработано: {data}'


class ValidationProcessor(BaseProcessor):
    def process(self, data):
        if data == '':
            return "Нет данных"
        else:
            return super().process(data)


class LoggingProcessor(BaseProcessor):
    def process(self, data):
        print(f'LOG: {data}')
        return super().process(data)


class DataService(LoggingProcessor, ValidationProcessor, BaseProcessor):
    pass


service = DataService()

print(service.process("Python"))
print(service.process(""))
print(DataService.mro())

