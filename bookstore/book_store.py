from member.member import Member
from member.member_dao_memory import MemberDAO
from member.member_service import MemberService
from book.book import Book
from book.book_dao import BookDAO
from book.book_service import BookService
from member.cart import CartItem

class BookStore:
    def __init__(self):
        self.book_id = 1
        self.book_store_menu = ["0. 종료", "1. 책 목록 보기", "2. 로그인", "3. 회원가입"]
        self.admin_menu_list = ["0. 로그아웃", "1. 회원 목록 조회 및 강퇴", "2. 도서 관리(등록/수정/삭제)"]
        self.admin_member_menu_list = ["0. 돌아가기", "1. 회원 강제 탈퇴(강퇴)"]
        self.admin_book_management_menu_list = ["0. 돌아가기", "1. 새 도서 등록", "2. 도서 정보 수정", "3. 기존 도서 삭제"]
        self.member_menu_list = ["0. 로그아웃", "1. 책 조회 및 구매/담기 선택", "2. 장바구니 확인 및 결제", "3. 주문 내역 조회", "4. 마이페이지 (배송지 변경/탈퇴)", "5. 비밀번호 변경"]
        self.book_select_menu_list = ["0. 돌아가기", "1. 장바구니에 담기", "2. 바로 주문하기"]
        self.member_mypage_menu_list = ["0. 돌아가기", "1. 기본 배송지(주소) 변경", "2. 회원 탈퇴 (서비스 해지)"]
        self.member_service = MemberService(MemberDAO())
        self.book_service = BookService(BookDAO())
        self.last_book_id_info()
        self.member_service.join(Member(self.member_service.ADMIN_ID, self.member_service.ADMIN_PASSWORD, "관리자", "성남시 수정구"))
        # self.init_dummy_books() # 더미데이터에용
        # self.init_dummy_members() # 이것도 더미데이터에용
        

    def last_book_id_info(self):
        book_list = self.book_service.get_book_list()
        if book_list:
            self.book_id = max(int(book.get_book_id()) for book in book_list) + 1


    # def init_dummy_books(self):
        # self.book_service.insert_book(Book(self.book_id,"파이썬 알고리즘", "홍길동", 25000, 5, "의진 출판"))
        # self.book_service.insert_book(Book(self.book_id,"자료구조 마스터", "권순범", 30000, 2, "의진 출판"))
        # self.book_service.insert_book(Book(self.book_id,"잡아스크립트", "배의진", 28000, 10, "의진 출판"))

    # def init_dummy_members(self):
        # self.member_service.join(Member("testuser", "1234", "홍길동", "서울"))
        # self.member_service.join(Member("kim", "1234", "김철수", "부산"))

    def show_menu(self,menu_list):
        for menu in menu_list:
            print(menu)
        print("-"*30)

    def run(self):
        while True:
            print("\n" + "-"*10 + "온라인 서점 메뉴" + "-"*10)
            self.show_menu(self.book_store_menu)
            choice = input("메뉴 선택: ")

            if choice == '1':
                self.just_show_books()
            elif choice == '2':
                self.login_menu()
            elif choice == '3':
                self.join_menu()
            elif choice == '0':
                print("\n프로그램을 종료합니다")
                break
            else:
                print("\n잘못된 입력입니다")

    def just_show_books(self):
        print("\n" + "-"*10 + "도서 목록" + "-"*10)
        books = self.book_service.get_book_list()
        if not books:
            print("현재 등록된 책이 없습니다")
        else:
            for b in books:
                print(b)
        print("-" * 10)

    def join_menu(self):
        print("\n" + "-"*10 + "회원 가입" + "-"*10)
        id = input("ID 입력: ")
        pw = input("비밀번호 입력: ")
        name = input("이름 입력: ")
        address = input("주소 입력: ")
        if self.member_service.join(Member(id, pw, name, address)):
            print("\n회원가입 성공!")
        else:
            print("\n회원가입 실패...")

    def login_menu(self):
        print("\n" + "-"*10 + "로그인" + "-"*10)
        id = input("ID: ")
        pw = input("Password: ")
        
        login_id = self.member_service.login(id, pw)
        if login_id:
            print(f"\n{login_id}님, 환영합니다!")
            if login_id == self.member_service.ADMIN_ID:
                self.admin_menu()
            else:
                self.member_menu()
        else:
            print("\n로그인 실패...")

    def admin_menu(self):
        while True:
            print("\n" + "-"*10 + "관리자 메뉴" + "-"*10)
            self.show_menu(self.admin_menu_list)
            menu = input("메뉴 선택: ")

            if menu == '1':
                self.admin_member_management()
            elif menu == '2':
                self.admin_book_management()
            elif menu == '0':
                self.member_service.logout()
                break
            else:
                print("\n잘못된 입력입니다")

    def admin_member_management(self):
        while True:
            print("\n" + "-"*10 + "전체 회원 관리" + "-"*10)
            members = self.member_service.list_member()
            for m in members:
                if m.get_id() != self.member_service.ADMIN_ID:
                    print(m)
            self.show_menu(self.admin_member_menu_list)
            menu = input("작업 선택: ")

            if menu == '1':
                self.admin_delete_member()
            elif menu == '0':
                break
    def admin_delete_member(self):
        member_id = input("강퇴할 회원의 ID를 입력하세요: ")
        if member_id == self.member_service.ADMIN_ID:
            print("관리자 계정은 삭제할 수 없습니다")
        else:
            if self.member_service.delete_account(member_id):
                print(f"\n{member_id}님이 강퇴 되었습니다")
            else:
                print("\n존재하지 않는 회원 ID입니다")

    def admin_book_management(self):
        while True:
            print("\n" + "-"*10 + "도서 관리" + "-"*10)
            self.show_menu(self.admin_book_management_menu_list)
            menu = input("메뉴 선택: ")

            if menu == '1':
                self.book_insert_info()
                    
            elif menu == '2':
                self.book_info_update()
                    
            elif menu == '3':
                self.book_info_delete()
            elif menu == '0':
                break
            else:
                print("\n잘못된 입력입니다")

    def book_insert_info(self):
        title = input("도서명: ")
        author = input("저자: ")
        price = int(input("가격: "))
        stock = int(input("재고: "))
        publisher = input("출판사: ")
        if self.book_service.insert_book(Book(self.book_id, title, author, price, stock, publisher)):
            self.book_id += 1
            print("\n도서 등록 완료")
        else:
            print("\n이미 존재하는 도서입니다")
    
    def book_info_update(self):
        book_id = input("수정할 도서의 id을 입력하세요: ")
        book = self.book_service.get_book_info(book_id)
        if book:
            print(f"기존 정보\n{book}")
            book.set_title(input("새 도서명: "))
            book.set_author(input("새 저자: "))
            book.set_price(int(input("새 가격: ")))
            book.set_stock(int(input("새 재고: ")))
            book.set_publisher(input("새 출판사: "))
            if self.book_service.update_book_info(book):
                print("\n도서 정보가 성공적으로 수정되었습니다")
        else:
            print("\n존재하지 않는 도서 번호입니다")

    def book_info_delete(self):
        book_id = input("삭제할 도서의 id을 입력하세요: ")
        if self.book_service.remove_book(book_id):
            print("\n도서가 성공적으로 삭제되었습니다")
        else:
            print("\n존재하지 않는 도서 번호입니다")

    def member_menu(self):
        while True:
            if self.member_service.current_user is None:
                break

            print("\n" + "-"*10 + "회원 메뉴" + "-"*10)
            self.show_menu(self.member_menu_list)
            menu = input("메뉴 선택: ")

            if menu == '1':
                self.member_book_selection()
            elif menu == '2':
                self.member_cart()
            elif menu == '3':
                self.show_order_history()
            elif menu == '4':
                self.member_mypage()
            elif menu == '5':
                self.menu_update_password()
            elif menu == '0':
                self.member_service.logout()
                print("\n로그아웃 되었습니다")
                break

    def member_book_selection(self):
        while True:
            print("\n" + "-"*10 + "회원용 도서 목록" + "-"*10)
            for i in self.book_service.get_book_list():
                print(i)
            print("-" * 45)
            
            book_id = input("원하시는 책의 번호를 입력하세요 (0번 입력 시 메뉴 탈출): ")
            if book_id == '0':
                break
                
            book = self.book_service.get_book_info(book_id)
            if not book:
                print("존재하지 않는 도서 번호입니다")
                continue

            print(f"\n선택하신 도서: {book.get_title()} (재고: {book.get_stock()}권)")
            self.show_menu(self.book_select_menu_list)
            action = input("원하시는 작업 선택: ")

            if action == '0':
                continue

            try:
                qty = int(input("구매/담기 수량을 입력하세요: "))
                if qty <= 0 or qty > book.get_stock():
                    print("수량이 부족하거나 올바르지 않습니다")
                    continue

                current_user = self.member_service.current_user

                if action == '1':
                    cart = current_user.get_cart()
                    already_in_cart = False
                    
                    for item in cart:
                        if item.get_book().get_book_id() == book.get_book_id():
                            item.set_quantity(item.get_quantity() + qty)
                            already_in_cart = True
                            break
                            
                    if not already_in_cart:
                        cart.append(CartItem(book, qty))
                        
                    print(f"\n'{book.get_title()}' {qty}권이 장바구니에 추가되었습니다")

                elif action == '2':
                    book.set_stock(book.get_stock() - qty)  
                    new_order = {
                        "items": [f"{book.get_title()} ({qty}권) [즉시 주문]"],
                        "total_price": book.get_price() * qty
                    }
                    current_user.get_order_list().append(new_order)
                    print(f"\n'{book.get_title()}' {qty}권의 즉시 주문 및 결제가 완료되었습니다!")

            except ValueError:
                print("숫자로만 입력해 주세요")

    def member_cart(self):
        current_user = self.member_service.current_user
        cart = current_user.get_cart()
        
        print("\n" + "-"*10 + "내 장바구니 목록" + "-"*10)
        if not cart:
            print("현재 장바구니가 비어 있습니다")
            print("-" * 45)
            return
        
        total_price = 0
        idx = 1
        
        for item in cart:
            b = item.get_book()
            q = item.get_quantity()
            sub_total = b.get_price() * q
            total_price += sub_total
            print(f"{idx}. {b.get_title()} | 수량: {q}권 | 합계: {sub_total}원")
            idx += 1  
            
        print(f"총 최종 결제 금액: {total_price}원")
        print(f"배송지: {current_user.get_address()}")

        menu = input("\n장바구니에 담긴 모든 상품을 최종 주문하시겠습니까? (Y/N): ").upper()
        if menu == 'Y':
            for item in cart:
                if item.get_quantity() > item.get_book().get_stock():
                    print(f"주문 실패: '{item.get_book().get_title()}'의 재고가 부족합니다")
                    return

            ordered_summary = []
            for item in cart:
                b = item.get_book()
                q = item.get_quantity()
                b.set_stock(b.get_stock() - q)  
                ordered_summary.append(f"{b.get_title()} ({q}권)")

            current_user.get_order_list().append({
                "items": ordered_summary,
                "total_price": total_price
            })
            current_user.clear_cart()  
            print(f"\n장바구니 상품이 [{current_user.get_address()}] 주소로 일괄 배송 처리되었습니다")

    def show_order_history(self):
        current_user = self.member_service.current_user
        orders = current_user.get_order_list()
        print("\n" + "-"*10 + " [ 내 주문 내역 ] " + "-"*10 )
        if not orders:
            print("주문하신 내역이 없습니다")
            return
        for idx, o in enumerate(orders, start=1):
            print(f"[{idx}번 주문] {', '.join(o['items'])} | 총 결제: {o['total_price']}원")
        print("-" * 45)

    def member_mypage(self):
        current_user = self.member_service.current_user
        while True:
            print("\n" + "-"*10 + "마이 페이지" + "-"*10)
            print(f"현재 로그인 ID: {current_user.get_id()}")
            print(f"등록된 기본 배송지: {current_user.get_address()}")
            self.show_menu(self.member_mypage_menu_list)
            menu = input("메뉴 선택: ")

            if menu == '1':
                new_addr = input("새로운 배송지 주소를 입력하세요: ")
                if self.member_service.update_address(current_user.get_id(), new_addr):
                    print("\n배송지 주소가 변경되었습니다")
                else:
                    print("\n주소 변경에 실패했습니다")
                    
            elif menu == '2':
                double_check = input("정말로 탈퇴하시겠습니까? 탈퇴 시 모든 장바구니와 주문 내역이 사라집니다 (Y/N): ").upper()
                if double_check == 'Y':
                    user_id = current_user.get_id()
                    self.member_service.logout()  
                    self.member_service.delete_account(user_id)  
                    print("\n회원 탈퇴가 완료되었습니다 이용해 주셔서 감사합니다")
                    break
            elif menu == '0':
                break
            
    def menu_update_password(self):
        org_password = input('>> 기존 비밀번호 입력 : ')
        new_password = input('>> 새 비밀번호 입력 : ')

        if self.member_service.update_password(self.member_service.current_user, org_password, new_password):
            print("\n비밀번호가 성공적으로 변경되었습니다")
        else:
            print("\n기존 비밀번호가 올바르지 않습니다")


if __name__ == '__main__':
    app = BookStore()
    app.run()