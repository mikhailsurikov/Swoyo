from datetime import datetime


class Contact:
    def __init__(self, name: str, phone: str, created_at=None):
        self.__name = name
        self.__phone = phone
        self.__created_at = created_at if created_at is not None else datetime.strftime(datetime.now(),
                                                                                        "%d.%m.%Y %H:%M")

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
    def __init__(self, relation: str, *args, created_at=None):
        self.__relation = relation
        self.__created_at = created_at if created_at is not None else datetime.strftime(datetime.now(),
                                                                                        "%d.%m.%Y %H:%M")
        super().__init__(*args)

    def __str__(self):
        return f'{self.get_name():<10} | {self.get_phone():<10} | {self.__relation:<10} ' \
               f'| {self.__created_at :<10}'

    def set_relation(self, relation):
        self.__relation = relation

    def to_dict(self):
        return {
            "type": "personal",
            "name": self.get_name(),
            "phone": self.get_phone(),
            "created_at": self.__created_at,
            "relation": self.__relation
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["phone"], data["relation"], data["created_at"])


class WorkContact(Contact):
    def __init__(self, company: str, *args, created_at=None):
        self.__company = company
        self.__created_at = created_at if created_at is not None else datetime.strftime(datetime.now(),
                                                                                        "%d.%m.%Y %H:%M")
        super().__init__(*args)

    def __str__(self):
        return f'{self.get_name():<10} | {self.get_phone():<10} | {self.__company:<10} ' \
               f'| {self.__created_at :<10}'

    def set_company(self, company):
        self.__company = company

    def to_dict(self):
        return {
            "type": "work",
            "name": self.get_name(),
            "phone": self.get_phone(),
            "created_at": self.__created_at,
            "company": self.__company
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["phone"], data["company"], data["created_at"])
