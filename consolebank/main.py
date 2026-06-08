from member.member import Member
from member.member_dao import MemberDAO
from member.member_service import MemberService

from account.account import Account
from account.account_dao import AccountDAO
from account.account_service import AccountService


class ConsoleBank:
    def __init__(self):
        self.msv = MemberService(MemberDAO())
        self.asv = AccountService(AccountDAO())

    def select_menu(self):
        try:
            menu = int(input('>> '))
            return menu
        except ValueError:
            return -1

    def run(self):
        while True:
            print()
            print('======== 콘솔 은행 ========')
            print('1. 로그인')
            print('2. 회원가입')
            print('0. 종료')

            menu = self.select_menu()

            if menu == 1:
                self.menu_login()

            elif menu == 2:
                self.menu_join()

            elif menu == 0:
                print('프로그램을 종료합니다')
                break

            else:
                print('잘못된 메뉴입니다')

    def menu_join(self):
        print()
        print('======== 회원가입 ========')

        id = input('아이디 : ')
        password = input('비밀번호 : ')
        name = input('이름 : ')

        member = Member(id, password, name)

        if self.msv.join(member):
            print('회원가입 완료')
        else:
            print('회원가입 실패')

    def menu_login(self):
        print()
        print('======== 로그인 ========')

        id = input('아이디 : ')
        password = input('비밀번호 : ')

        if self.msv.login(id, password):
            print('로그인 성공')

            if id == MemberService.ADMIN_ID:
                self.run_admin_menu()
            else:
                self.run_banking_menu()
        else:
            print('로그인 실패')

    def run_banking_menu(self):
        while True:
            print()
            print('======== 은행 메뉴 ========')
            print('1. 계좌목록')
            print('2. 입금')
            print('3. 출금')
            print('4. 송금')
            print('5. 계좌생성')
            print('6. 계좌해지')
            print('7. 내정보')
            print('0. 로그아웃')

            menu = self.select_menu()

            if menu == 1:
                self.menu_my_account_list()

            elif menu == 2:
                self.menu_deposit()

            elif menu == 3:
                self.menu_withdraw()

            elif menu == 4:
                self.menu_transfer()

            elif menu == 5:
                self.menu_create_account()

            elif menu == 6:
                self.menu_delete_account()

            elif menu == 7:
                self.run_my_info_menu()

            elif menu == 0:
                self.msv.logout()
                print('로그아웃 되었습니다')
                break

            else:
                print('잘못된 메뉴입니다')

    def menu_my_account_list(self):
        print()
        print('======== 내 계좌 목록 ========')

        account_list = self.asv.get_member_account(self.msv.current_user)

        if len(account_list) == 0:
            print('계좌가 없습니다')
            return

        for account in account_list:
            print(account)

    def menu_create_account(self):
        print()
        print('======== 계좌 생성 ========')

        password = input('계좌 비밀번호 : ')

        account = Account(
            '',
            self.msv.current_user,
            0,
            password
        )

        if self.asv.create_account(account):
            print('계좌 생성 완료')
        else:
            print('계좌 생성 실패')

    def menu_deposit(self):
        print()
        print('======== 입금 ========')

        self.menu_my_account_list()

        account_no = input('계좌번호 : ')

        try:
            amount = int(input('입금액 : '))
        except ValueError:
            print('금액은 숫자로 입력하세요')
            return

        result = self.asv.deposit(account_no, amount)

        if result == 0:
            print('없는 계좌입니다')

        elif result == 1:
            print('입금액은 0원보다 커야 합니다')

        elif result == 2:
            print('입금 완료')
            print(f'잔액 : {self.asv.get_account_balance(account_no):,}원')

    def menu_withdraw(self):
        print()
        print('======== 출금 ========')

        self.menu_my_account_list()

        account_no = input('계좌번호 : ')

        try:
            amount = int(input('출금액 : '))
        except ValueError:
            print('금액은 숫자로 입력하세요')
            return

        password = input('계좌 비밀번호 : ')

        result = self.asv.withdraw(
            self.msv.current_user,
            account_no,
            amount,
            password
        )

        if result == 0:
            print('없는 계좌입니다')

        elif result == 1:
            print('본인 계좌가 아닙니다')

        elif result == 2:
            print('비밀번호가 틀렸습니다')

        elif result == 3:
            print('출금액은 0원보다 커야 합니다')

        elif result == 4:
            print('잔액이 부족합니다')

        elif result == 5:
            print('출금 완료')
            print(f'잔액 : {self.asv.get_account_balance(account_no):,}원')

    def menu_transfer(self):
        print()
        print('======== 송금 ========')

        self.menu_my_account_list()

        from_account_no = input('보낼 계좌번호 : ')
        to_account_no = input('받을 계좌번호 : ')

        try:
            amount = int(input('송금액 : '))
        except ValueError:
            print('금액은 숫자로 입력하세요')
            return

        password = input('계좌 비밀번호 : ')

        result = self.asv.transfer(
            self.msv.current_user,
            from_account_no,
            to_account_no,
            amount,
            password
        )

        if result == 0:
            print('보낼 계좌가 없습니다')

        elif result == 1:
            print('받을 계좌가 없습니다')

        elif result == 2:
            print('본인 계좌가 아닙니다')

        elif result == 3:
            print('비밀번호가 틀렸습니다')

        elif result == 4:
            print('송금액은 0원보다 커야 합니다')

        elif result == 5:
            print('잔액이 부족합니다')

        elif result == 6:
            print('송금 완료')
            print(f'잔액 : {self.asv.get_account_balance(from_account_no):,}원')

    def menu_delete_account(self):
        print()
        print('======== 계좌 해지 ========')

        self.menu_my_account_list()

        account_no = input('해지할 계좌번호 : ')
        password = input('계좌 비밀번호 : ')

        result = self.asv.delete_account(
            self.msv.current_user,
            account_no,
            password
        )

        if result == 0:
            print('없는 계좌입니다')

        elif result == 1:
            print('본인 계좌가 아닙니다')

        elif result == 2:
            print('비밀번호가 틀렸습니다')

        elif result == 3:
            print('계좌 해지 완료')

        elif result == 4:
            print('잔액이 남아있는 계좌는 해지할 수 없습니다')

    def run_my_info_menu(self):
        while True:
            print()
            print('======== 내 정보 ========')
            print('1. 내 정보 보기')
            print('2. 비밀번호 변경')
            print('3. 회원탈퇴')
            print('0. 돌아가기')

            menu = self.select_menu()

            if menu == 1:
                member = self.msv.view_member_info(self.msv.current_user)
                print(member)

            elif menu == 2:
                self.menu_change_password()

            elif menu == 3:
                if self.menu_withdraw_member():
                    break

            elif menu == 0:
                break

            else:
                print('잘못된 메뉴입니다')

    def menu_change_password(self):
        print()
        print('======== 비밀번호 변경 ========')

        old_password = input('기존 비밀번호 : ')
        new_password = input('새 비밀번호 : ')

        if self.msv.change_password(
            self.msv.current_user,
            old_password,
            new_password
        ):
            print('비밀번호 변경 완료')
        else:
            print('비밀번호 변경 실패')

    def menu_withdraw_member(self):
        print()
        print('======== 회원탈퇴 ========')

        password = input('비밀번호 확인 : ')
        member = self.msv.view_member_info(self.msv.current_user)

        if member.get_password() != password:
            print('비밀번호가 틀렸습니다')
            return False

        user_id = self.msv.current_user

        # Try to delete all accounts for the user; abort if any account has balance
        if not self.asv.delete_account_by_member_id(user_id):
            print('잔액이 남아있는 계좌가 있어 회원탈퇴할 수 없습니다')
            return False

        if not self.msv.delete_member(user_id):
            print('회원탈퇴 실패')
            return False

        self.msv.logout()

        print('회원탈퇴 완료')
        return True

    def run_admin_menu(self):
        while True:
            print()
            print('======== 관리자 메뉴 ========')
            print('1. 회원목록')
            print('2. 회원조회')
            print('3. 회원삭제')
            print('4. 전체계좌목록')
            print('5. 회원별계좌목록')
            print('0. 로그아웃')

            menu = self.select_menu()

            if menu == 1:
                self.menu_all_member_list()

            elif menu == 2:
                self.menu_member_info()

            elif menu == 3:
                self.menu_admin_delete_member()

            elif menu == 4:
                self.menu_all_account_list()

            elif menu == 5:
                self.menu_member_account_list()

            elif menu == 0:
                self.msv.logout()
                print('로그아웃 되었습니다')
                break

            else:
                print('잘못된 메뉴입니다')

    def menu_all_member_list(self):
        print()
        print('======== 전체 회원 목록 ========')

        member_list = self.msv.view_all_member()

        for member in member_list:
            print(member)

    def menu_member_info(self):
        print()
        print('======== 회원 조회 ========')

        id = input('조회할 아이디 : ')
        member = self.msv.view_member_info(id)

        if member is None:
            print('없는 회원입니다')
        else:
            print(member)

    def menu_admin_delete_member(self):
        print()
        print('======== 회원 삭제 ========')

        id = input('삭제할 아이디 : ')

        member = self.msv.view_member_info(id)

        if member is None:
            print('없는 회원입니다')
            return

        if id == MemberService.ADMIN_ID:
            print('관리자는 삭제할 수 없습니다')
            return

        # Ensure member's accounts can be deleted (no remaining balance)
        if not self.asv.delete_account_by_member_id(id):
            print('잔액이 남아있는 계좌가 있어 회원 삭제 불가')
            return

        if self.msv.delete_member(id):
            print('회원 삭제 완료')
        else:
            print('회원 삭제 실패')

    def menu_all_account_list(self):
        print()
        print('======== 전체 계좌 목록 ========')

        account_list = self.asv.get_all_account()

        if len(account_list) == 0:
            print('계좌가 없습니다')
            return

        for account in account_list:
            print(account)

    def menu_member_account_list(self):
        print()
        print('======== 회원별 계좌 목록 ========')

        id = input('조회할 회원 아이디 : ')

        account_list = self.asv.get_member_account(id)

        if len(account_list) == 0:
            print('계좌가 없습니다')
            return

        for account in account_list:
            print(account)


if __name__ == '__main__':
    app = ConsoleBank()
    app.run()