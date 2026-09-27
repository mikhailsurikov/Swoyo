from datetime import datetime


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
    def __init__(self, name: str, phone: str, relation: str, created_at=None):
        super().__init__(name, phone)
        self.relation = relation
        self.__created_at = created_at if created_at is not None else datetime.now().strftime("%d.%m.%Y %H:%M")

    def __str__(self):
        return f'{self.get_name():<10} | {self.get_phone():<10} | {self.relation:<10} ' \
               f'| {self.__created_at :<10}'

    def set_relation(self, relation):
        self.relation = relation

    def to_dict(self):
        return {
            "type": "personal",
            "name": self.get_name(),
            "phone": self.get_phone(),
            "created_at": self.__created_at,
            "relation": self.relation
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["phone"], data["relation"], created_at=data["created_at"])


class WorkContact(Contact):
    def __init__(self, name: str, phone: str, company: str, created_at=None):
        super().__init__(name, phone)
        self.company = company
        self.__created_at = created_at if created_at is not None else datetime.now().strftime("%d.%m.%Y %H:%M")

    def __str__(self):
        return f'{self.get_name():<10} | {self.get_phone():<10} | {self.company:<10} ' \
               f'| {self.__created_at :<10}'

    def set_company(self, company):
        self.company = company

    def to_dict(self):
        return {
            "type": "work",
            "name": self.get_name(),
            "phone": self.get_phone(),
            "created_at": self.__created_at,
            "company": self.company
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["phone"], data["company"], created_at=data["created_at"])
