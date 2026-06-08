import json
import os
from account.account import Account


class AccountDAO:
    def __init__(self):
        self.__file_path = 'data/accounts.json'
        self.__account_db = self.__load()

    def __load(self):
        if not os.path.exists(self.__file_path):
            return {}

        with open(self.__file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        result = {}

        for account_no, account_data in data.items():
            result[account_no] = Account.from_dict(account_data)

        return result

    def __save(self):
        data = {}

        for account_no, account in self.__account_db.items():
            data[account_no] = account.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def insert_account(self, account):
        self.__account_db[account.get_account_no()] = account
        self.__save()
        return True

    def select_account(self, account_no):
        return self.__account_db.get(account_no)

    def select_all_account(self):
        return list(self.__account_db.values())

    def select_account_by_member_id(self, member_id):
        result = []

        for account in self.__account_db.values():
            if account.get_owner() == member_id:
                result.append(account)

        return result

    def update_account(self, account_no, account):
        self.__account_db[account_no] = account
        self.__save()
        return True

    def delete_account(self, account_no):
        if account_no in self.__account_db:
            del self.__account_db[account_no]
            self.__save()
            return True

        return False

    def delete_account_by_member_id(self, member_id):
        delete_list = []

        for account_no, account in self.__account_db.items():
            if account.get_owner() == member_id:
                delete_list.append(account_no)

        for account_no in delete_list:
            del self.__account_db[account_no]

        self.__save()
        return True