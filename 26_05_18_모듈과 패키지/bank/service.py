from .models import Account


class AccountService:
    def __init__(self, member_service=None):
        self.__account_list = []
        self._member_service = member_service

    def create_account(self, account_no, owner, balance):
        if self._member_service is not None:
            member = self._member_service.member_detail(owner)
            if not member:
                return False

        account = Account(account_no, owner, balance)
        self.__account_list.append(account)
        return True

    def list_account(self):
        return self.__account_list
    
    def deposit(self, account_no, amount):  
        for account in self.__account_list: 
            if account.get_account_no() == account_no:
                account.deposit(amount)
                break
    def withdraw(self, account_no, amount):
        for account in self.__account_list:
            if account.get_account_no() == account_no:
                account.withdraw(amount)
                return True
        return False
