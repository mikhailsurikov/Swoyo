class Contact:
    def __init__(self, name: str, phone: str):
        self.__name = name
        self.__phone = phone

    def set_name(self, name):
        self.__name = name

    def set_phone(self, phone):
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    def __str__(self):
        return f'{self.get_name():<10} | {self.get_phone()}'


class PersonalContact(Contact):
    def __init__(self, relation: str, *args):
        self.__relation = relation
        super().__init__(*args)

    def __str__(self):
        return f'{self.get_name():<10} | {self.get_phone():<10} | {self.__relation}'

    def set_relation(self, relation):
        self.__relation = relation


class WorkContact(Contact):
    def __init__(self, company: str, *args):
        self.__company = company
        super().__init__(*args)

    def __str__(self):
        return f'{self.get_name():<10} | {self.get_phone():<10} | {self.__company}'

    def set_company(self, company):
        self.__company = company
