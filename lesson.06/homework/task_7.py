# Задание 7. Обработка уведомлений
# Создайте родительский класс:
# Notification
# Он принимает текст сообщения и содержит метод:
# send()
# Создайте два дочерних класса:
# EmailNotification
# SmsNotification
# Переопределите метод send().
# После этого создайте список:
# С помощью одного цикла:
# 1. вызовите `send()` у каждого объекта;
# 2. с помощью `isinstance()` посчитайте количество Email- и SMS-уведомлений.

class Notification:
    def __init__(self, text):
        self.text = text

    def send(self):
        pass


class EmailNotification(Notification):
    def send(self):
        print('Email: ' + self.text)


class SmsNotification(Notification):
    def send(self):
        print('SMS: ' + self.text)


notifications = [
    EmailNotification("Первое сообщение"),
    SmsNotification("Второе сообщение"),
    EmailNotification("Третье сообщение")]

emails = 0
sms = 0
for i in notifications:
    i.send()
    emails += isinstance(i, EmailNotification)
    sms += isinstance(i, SmsNotification)
print(
    f'Email: {emails} \nSMS: {sms}')
