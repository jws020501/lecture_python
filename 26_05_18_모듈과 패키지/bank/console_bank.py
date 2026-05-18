from bank.service import AccountService


# 메뉴와 사용자 interaction에 따른 서비스 호출
def select_menu():
    print('========================================================')
    print(' 1. 계좌생성 | 2. 계좌목록 | 3. 입금 | 4. 출금 | 0. 종료')
    print('========================================================')
    try:
        menu = int(input('>> 메뉴 선택 : '))
    except ValueError:
        menu = -1
    return menu

def run_console(member_service=None):
    # create AccountService with optional MemberService for validation
    aservice = AccountService(member_service=member_service)

    print()
    print('============== Wonseok Bank ==============')
    while True:
        menu = select_menu()
        if menu == 0:
            break

        elif menu == 1:
            # 계좌번호, 계좌주, 잔액 입력을 받아서 계좌 생성
            account_no = input("> 계좌번호 : ")
            owner = input("> 계좌주 : ")
            try:
                balance = int(input("> 초기입금액 : "))
            except ValueError:
                print('잘못된 금액입니다.')
                continue

            if aservice.create_account(account_no, owner, balance):
                print('결과 : 계좌가 생성되었습니다.')
            else:
                print('결과 : 일치하는 회원이 없습니다. 계좌를 생성할 수 없습니다.')

        elif menu == 2: # 계좌목록
            account_list = aservice.list_account()
            print('------------')
            print(' 계좌 목록')
            print('------------')
            for account in account_list:
                print(account)

        elif menu == 3: # 입금
            print('------------')
            print(' 예금 ')
            print('------------')
            account_no = input('> 계좌번호')
            try:
                amount = int(input('> 예금액 : '))
            except ValueError:
                print('잘못된 금액입니다.')
                continue
            aservice.deposit(account_no, amount)
        else: #출금
            print('------------')
            print(' 출금 ')
            print('------------')
            account_no = input('> 계좌번호')
            try:
                amount = int(input('> 출금액 : '))
            except ValueError:
                print('잘못된 금액입니다.')
                continue

            if aservice.withdraw(account_no, amount):
                print('결과: 출금이 성공되었습니다.')
            else:
                print('결과: 일치하는 계좌번호가 없습니다.')

    print('======== 이용해 주셔서 감사합니다. ========')


if __name__ == '__main__':
    run_console()
