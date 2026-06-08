class Account:
    def __init__(self, account_no, owner, balance, password):
        self.__account_no = account_no
        self.__owner = owner
        self.__balance = balance
        self.__password = password

    def get_account_no(self):
        return self.__account_no

    def get_owner(self):
        return self.__owner

    def get_balance(self):
        return self.__balance

    def get_password(self):
        return self.__password

    def set_account_no(self, account_no):
        self.__account_no = account_no

    def set_balance(self, balance):
        self.__balance = balance

    def __str__(self):
        return f'계좌번호 = {self.__account_no} 계좌주 = {self.__owner} 잔액 = {self.__balance:,}원'
    def to_dict(self):
        return {
            'account_no': self.__account_no,
            'owner': self.__owner,
            'balance': self.__balance,
            'password': self.__password
        }

    @staticmethod
    def from_dict(data):
        return Account(
            data['account_no'],
            data['owner'],
            data['balance'],
            data['password']
        )