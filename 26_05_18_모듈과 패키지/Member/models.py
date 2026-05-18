class Member:
    def __init__(self, member_no, member_id, pw, name, call_no, address):
        self.__member_no = member_no
        self.__member_id = member_id
        self.__pw = pw
        self.__name = name
        self.__call_no = call_no
        self.__address = address
        
    def __str__(self):
        return f'{self.__member_no}\t{self.__member_id}\t{self.__pw}\t{self.__name}\t{self.__call_no}\t{self.__address}'

    def get_member_no(self):
        return self.__member_no
    def get_member_id(self):
        return self.__member_id
    def get_pw(self):
        return self.__pw
    def get_name(self):
        return self.__name
    def get_call_no(self):
        return self.__call_no
    def get_address(self):
        return self.__address

    def set_pw(self, pw):
        self.__pw = pw
    def set_name(self, name):
        self.__name = name
    def set_call_no(self, call_no):
        self.__call_no = call_no
    def set_address(self, address):
        self.__address = address
