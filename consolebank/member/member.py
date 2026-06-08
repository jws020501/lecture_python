class Member:
    def __init__(self, id, password, name):
        self.__id = id
        self.__password = password
        self.__name = name

    def get_id(self):
        return self.__id

    def get_password(self):
        return self.__password

    def get_name(self):
        return self.__name

    def set_password(self, password):
        self.__password = password

    def __str__(self):
        return f'아이디 = {self.__id} 이름 = {self.__name}'
    
    def to_dict(self):
        return {
            'id': self.__id,
            'password': self.__password,
            'name': self.__name
        }

    @staticmethod
    def from_dict(data):
        return Member(
            data['id'],
            data['password'],
            data['name']
        )