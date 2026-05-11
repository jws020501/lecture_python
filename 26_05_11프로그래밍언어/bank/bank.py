from datetime import datetime

class BankAccount:
    def __init__(self, account, name, balance=0):
        self.account = account
        self.name = name
        self.balance = balance
        self.create_at = datetime.now()
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("입금액은 0보다 커야 합니다.")
            return
        self.balance += amount
        self.transactions.append({"type": "입금", "amount": amount, "date": datetime.now()})
        print(f"[입금] {amount:,}원 | 잔액: {self.balance:,}원")

    def withdraw(self, amount):
        if amount <= 0:
            print("출금액은 0보다 커야 합니다.")
            return
        if amount > self.balance:
            print("잔액이 부족합니다.")
            return
        self.balance -= amount
        self.transactions.append({"type": "출금", "amount": amount, "date": datetime.now()})
        print(f"[출금] {amount:,}원 | 잔액: {self.balance:,}원")

    def get_balance(self):
        print(f"[{self.name}] 계좌번호: {self.account} | 잔액: {self.balance:,}원")
        return self.balance

    def get_history(self):
        print(f"=== [{self.name}] 거래 내역 ===")
        if not self.transactions:
            print("거래 내역이 없습니다.")
            return
        for t in self.transactions:
            print(f"{t['date'].strftime('%Y-%m-%d %H:%M:%S')} | {t['type']} | {t['amount']:,}원")

    def __str__(self):
        return f"BankAccount(계좌: {self.account}, 예금주: {self.name}, 잔액: {self.balance:,}원)"


def select_menu():
    print("=======================================================")
    print("1. 계좌 생성 | 2. 계좌 목록 | 3. 입금 | 4. 출금 | 0. 종료")
    print("=======================================================")


def create_account(accounts):
    account = input("계좌번호: ")
    if account in accounts:
        print("이미 존재하는 계좌입니다.")
        return
    name = input("예금주명: ")
    balance = input("초기입금액(선택): ")
    balance = int(balance) if balance else 0
    
    accounts[account] = BankAccount(account, name, balance)
    print(f"✓ 계좌가 생성되었습니다.\n{accounts[account]}\n")


def list_accounts(accounts):
    if not accounts:
        print("등록된 계좌가 없습니다.\n")
        return
    
    print("\n=== 계좌 목록 ===")
    for account in accounts.values():
        print(account)
    print()


def deposit_money(accounts):
    account = input("계좌번호: ")
    if account not in accounts:
        print("존재하지 않는 계좌입니다.\n")
        return
    
    try:
        amount = int(input("입금액: "))
        accounts[account].deposit(amount)
    except ValueError:
        print("숫자를 입력해주세요.\n")


def withdraw_money(accounts):
    account = input("계좌번호: ")
    if account not in accounts:
        print("존재하지 않는 계좌입니다.\n")
        return
    
    try:
        amount = int(input("출금액: "))
        accounts[account].withdraw(amount)
    except ValueError:
        print("숫자를 입력해주세요.\n")


accounts = {}
while True:
    select_menu()
    select = input("메뉴를 선택해주십시오: ")
    
    if select == "1":
        create_account(accounts)
    elif select == "2":
        list_accounts(accounts)
    elif select == "3":
        deposit_money(accounts)
    elif select == "4":
        withdraw_money(accounts)
    elif select == "0":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 선택입니다. 다시 선택해주세요.\n")
