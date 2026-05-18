from bank.console_bank import run_console as run_bank_console
from Member.member_manager import run_console as run_member_console
from Member.service import MemberService


def select_main_menu():
    print('================= MAIN MENU =================')
    print(' 1. 은행 관리 | 2. 회원 관리 | 0. 종료')
    print('=============================================')
    try:
        return int(input('>> 선택 : '))
    except ValueError:
        return -1


def main():
    member_service = MemberService()
    while True:
        choice = select_main_menu()
        if choice == 0:
            print('프로그램을 종료합니다.')
            break
        elif choice == 1:
            try:
                run_bank_console(member_service)
            except Exception as e:
                print('은행 기능 실행 중 오류:', e)
        elif choice == 2:
            try:
                run_member_console(member_service)
            except Exception as e:
                print('회원 기능 실행 중 오류:', e)
        else:
            print('올바른 메뉴를 선택하세요.')


if __name__ == '__main__':
    main()
