# Задание 10 ⭐. Способы оплаты
# Создайте родительский класс:
# Payment
# Он принимает сумму покупки.
# Создайте дочерние классы:
# CashPayment
# CardPayment
# BonusPayment
# Во всех классах переопределите метод:
# get_final_amount()
# ### Правила
# При оплате наличными сумма не изменяется.
# При оплате картой добавляется комиссия `2%`.
# При оплате бонусами действует скидка `10%`.

class Payment:
    def __init__(self, amount):
        self.amount = amount

    def get_final_amount(self):
        pass


class CashPayment(Payment):
    def get_final_amount(self):
        return self.amount


class CardPayment(Payment):
    def get_final_amount(self):
        return self.amount * 1.02


class BonusPayment(Payment):
    def get_final_amount(self):
        return self.amount * 0.9


payments = [
    CashPayment(1000),
    CardPayment(1000),
    BonusPayment(1000)
]

for payment in payments:
    print(payment.get_final_amount())
