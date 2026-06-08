class AccountService:
    account_no_seq = 111111

    def __init__(self, account_dao):
        self.__dao = account_dao
        self.__init_account_no_seq()
        
    def create_account(self, account):
        account.set_account_no(str(AccountService.account_no_seq))
        AccountService.account_no_seq += 1

        return self.__dao.insert_account(account)

    def get_account(self, account_no):
        return self.__dao.select_account(account_no)

    def get_all_account(self):
        return self.__dao.select_all_account()

    def get_member_account(self, member_id):
        return self.__dao.select_account_by_member_id(member_id)

    def get_account_balance(self, account_no):
        account = self.get_account(account_no)

        if account is None:
            return 0

        return account.get_balance()

    def deposit(self, account_no, amount):
        account = self.get_account(account_no)

        if account is None:
            return 0

        if amount <= 0:
            return 1

        account.set_balance(account.get_balance() + amount)
        self.__dao.update_account(account_no, account)

        return 2

    def withdraw(self, member_id, account_no, amount, password):
        account = self.get_account(account_no)

        if account is None:
            return 0

        if account.get_owner() != member_id:
            return 1

        if account.get_password() != password:
            return 2

        if amount <= 0:
            return 3

        if account.get_balance() < amount:
            return 4

        account.set_balance(account.get_balance() - amount)
        self.__dao.update_account(account_no, account)

        return 5

    def transfer(self, member_id, from_account_no, to_account_no, amount, password):
        from_account = self.get_account(from_account_no)
        to_account = self.get_account(to_account_no)

        if from_account is None:
            return 0

        if to_account is None:
            return 1

        if from_account.get_owner() != member_id:
            return 2

        if from_account.get_password() != password:
            return 3

        if amount <= 0:
            return 4

        if from_account.get_balance() < amount:
            return 5

        from_account.set_balance(from_account.get_balance() - amount)
        to_account.set_balance(to_account.get_balance() + amount)

        self.__dao.update_account(from_account_no, from_account)
        self.__dao.update_account(to_account_no, to_account)

        return 6

    def delete_account(self, member_id, account_no, password):
        account = self.get_account(account_no)

        if account is None:
            return 0

        if account.get_owner() != member_id:
            return 1

        if account.get_password() != password:
            return 2

        # Prevent deletion if account still has balance
        if account.get_balance() > 0:
            return 4

        self.__dao.delete_account(account_no)

        return 3

    def delete_account_by_member_id(self, member_id):
        # Do not delete any accounts if any account for the member has non-zero balance
        for account in self.get_member_account(member_id):
            if account.get_balance() > 0:
                return False

        return self.__dao.delete_account_by_member_id(member_id)

    def __init_account_no_seq(self):
        account_list = self.__dao.select_all_account()

        if len(account_list) == 0:
            AccountService.account_no_seq = 111111
            return

        max_no = 0

        for account in account_list:
            account_no = int(account.get_account_no())

            if account_no > max_no:
                max_no = account_no

        AccountService.account_no_seq = max_no + 1