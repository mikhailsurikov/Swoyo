# Задание 2. Дата доставки
# Дана дата отправки заказа:
# order_date = "05.09.2026"
# И срок доставки:
# delivery_days = 14
# Используя `datetime`:
# 1. преобразуйте строку в дату;
# 2. прибавьте количество дней;
# 3. выведите дату доставки в формате `дд.мм.гггг`.

import datetime

order_date = "05.09.2026"
delivery_days = 14
print(
    (datetime.datetime.strptime(order_date, "%d.%m.%Y") + datetime.timedelta(days=delivery_days)).strftime("%d.%m.%Y"))
