from member.member import Member
from account.account_service import AccountService


class MemberService:
    ADMIN_ID = 'admin'
    ADMIN_PASSWORD = '1234'

    def __init__(self, member_dao):
        self.__dao = member_dao
        self.current_user = None

        admin = Member(
            MemberService.ADMIN_ID,
            MemberService.ADMIN_PASSWORD,
            '관리자'
        )

        self.__dao.insert_member(admin)

    def join(self, member):
        if member.get_id() == MemberService.ADMIN_ID:
            return False

        if self.__dao.select_member(member.get_id()) is not None:
            return False

        if member.get_id().strip() == '':
            return False

        if member.get_password().strip() == '':
            return False

        return self.__dao.insert_member(member)

    def login(self, id, password):
        member = self.__dao.select_member(id)

        if member is None:
            return False

        if member.get_password() != password:
            return False

        self.current_user = id
        return True

    def logout(self):
        self.current_user = None

    def view_member_info(self, id):
        return self.__dao.select_member(id)

    def view_all_member(self):
        return self.__dao.select_all_member()

    def change_password(self, id, old_password, new_password):
        member = self.__dao.select_member(id)

        if member is None:
            return False

        if member.get_password() != old_password:
            return False

        member.set_password(new_password)
        return self.__dao.update_member(member)

    def delete_member(self, id):
        if id == MemberService.ADMIN_ID:
            return False
        if self.current_user != id:
            return False
        account = AccountService.get_member_account(id)
        account_money = 0
        for acc in account:
            account_money += acc.get_balance()
        if account_money > 0:
            return False
        return self.__dao.delete_member(id)