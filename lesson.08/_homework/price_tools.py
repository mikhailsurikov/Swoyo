def apply_discount(price, percent):
    return round(price * (1 - percent / 100), 0)


if __name__ == '__main__':
    print(apply_discount(250, 30))
    print(apply_discount(40, 90))
    print(apply_discount(1000, 20))
