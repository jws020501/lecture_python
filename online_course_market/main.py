from market_service import MarketService
from validation import clean_text


def print_line():
    print("-" * 40)


def input_number(text):
    value = input(text).strip()
    if value.isdigit():
        return int(value)
    return 0


def print_users(market):
    print_line()
    print("[회원 목록]")
    users = market.users.list_users()
    if len(users) == 0:
        print("등록된 회원이 없습니다.")
    for user in users:
        print(
            user["id"],
            "아이디:",
            user.get("login_id", ""),
            "이름:",
            user["name"],
            "역할:",
            user["role"],
            "전화:",
            user.get("phone", ""),
            "이메일:",
            user.get("email", ""),
        )


def print_courses(courses):
    print_line()
    print("[강의 목록]")
    if len(courses) == 0:
        print("등록된 강의가 없습니다.")
    for course in courses:
        print(
            course["id"],
            course["title"],
            course["category"],
            str(course["price"]) + "원",
            course["status"],
            "영상수:",
            len(course["lectures"]),
        )


def print_current_user(current_user):
    if current_user is None:
        print("현재 상태: 비로그인")
    else:
        print("현재 사용자:", current_user["id"], current_user["name"], current_user["role"])


def print_orders(market):
    print_line()
    print("[구매 목록]")
    orders = market.purchases.list_orders()
    if len(orders) == 0:
        print("구매 내역이 없습니다.")
    for order in orders:
        course = market.courses.find_course(order["course_id"])
        if course is None:
            course_title = "삭제된 강의"
        else:
            course_title = course["title"]
        rate = market.purchases.get_progress_rate(order["student_id"], order["course_id"])
        print(
            order["id"],
            "수강생ID:",
            order["student_id"],
            "강의:",
            course_title,
            "가격:",
            str(order.get("price", 0)) + "원",
            "진도율:",
            str(rate) + "%",
        )


def user_menu(market):
    print_line()
    print("[회원 가입]")
    print("로그인에 사용할 정보를 입력하세요.")

    login_id = input("아이디: ").strip()
    if login_id == "":
        print("아이디는 비워둘 수 없습니다.")
        return
    if market.users.is_login_id_used(login_id):
        print("이미 사용 중인 아이디입니다.")
        return

    password = input("비밀번호: ").strip()
    if password == "":
        print("비밀번호는 비워둘 수 없습니다.")
        return

    password_check = input("비밀번호 확인: ").strip()
    if password != password_check:
        print("비밀번호 확인이 일치하지 않습니다.")
        return

    name = input("이름: ").strip()
    if name == "":
        print("이름은 비워둘 수 없습니다.")
        return

    phone = input("전화번호: ").strip()
    email = input("이메일: ").strip()

    print("1. 수강생")
    print("2. 강사")
    print("3. 관리자")
    choice = input("역할 선택: ").strip()

    if choice == "1":
        role = "수강생"
    elif choice == "2":
        role = "강사"
    elif choice == "3":
        role = "관리자"
    else:
        print("역할은 관리자, 강사, 수강생 중 하나여야 합니다.")
        return

    user = market.users.create_user(name, role, login_id, password, phone, email)
    if user is None:
        print("회원 가입에 실패했습니다. 입력값을 확인하세요.")
        return
    print("회원 가입 완료")
    print("회원 번호:", user["id"])
    print("아이디:", user["login_id"])
    print("이름:", user["name"])
    print("역할:", user["role"])


def login_menu(market):
    print_line()
    print("[로그인]")
    print("샘플 계정: admin/admin1234, teacher/teacher1234, student/student1234")
    login_id = input("아이디: ").strip()
    password = input("비밀번호: ").strip()

    user, message = market.users.login(login_id, password)
    print(message)
    if user is None:
        return None

    print("현재 사용자:", user["name"], user["role"])
    return user


def logout_menu():
    print_line()
    print("로그아웃되었습니다.")
    return None


def course_menu(market, current_user=None):
    print_line()
    print("[강의 등록]")
    if current_user is None:
        instructor_id = input_number("강사 ID: ")
    else:
        instructor_id = current_user["id"]
    title = input("강의명: ").strip()
    category = input("카테고리: ").strip()
    price = input_number("가격: ")

    course, message = market.courses.create_course(instructor_id, title, category, price)
    print(message)
    if course is not None:
        print("강의 ID:", course["id"])


def lecture_menu(market, current_user=None):
    print_line()
    print("[강의 영상 추가]")
    if current_user is None:
        instructor_id = input_number("강사 ID: ")
    else:
        instructor_id = current_user["id"]
    course_id = input_number("강의 ID: ")
    title = input("영상 제목: ").strip()

    lecture, message = market.courses.add_lecture(instructor_id, course_id, title)
    print(message)
    if lecture is not None:
        print("영상 ID:", lecture["id"])


def approve_menu(market, current_user=None):
    print_line()
    print("[강의 승인]")
    if current_user is None:
        admin_id = input_number("관리자 ID: ")
    else:
        admin_id = current_user["id"]
    course_id = input_number("강의 ID: ")

    course, message = market.courses.approve_course(admin_id, course_id)
    print(message)


def search_menu(market):
    print_line()
    print("[강의 검색]")
    keyword = input("검색어: ").strip()
    courses = market.courses.search_courses(keyword)
    print_courses(courses)


def buy_menu(market, current_user=None):
    print_line()
    print("[강의 구매]")
    if current_user is None:
        student_id = input_number("수강생 ID: ")
    else:
        student_id = current_user["id"]
    course_id = input_number("강의 ID: ")

    order, message = market.purchases.buy_course(student_id, course_id)
    print(message)


def progress_menu(market, current_user=None):
    print_line()
    print("[수강 완료]")
    if current_user is None:
        student_id = input_number("수강생 ID: ")
    else:
        student_id = current_user["id"]
    course_id = input_number("강의 ID: ")
    course = market.courses.find_course(course_id)

    if course is None:
        print("강의를 찾을 수 없습니다.")
        return

    print("[영상 목록]")
    for lecture in course["lectures"]:
        print(lecture["id"], lecture["title"])

    lecture_id = input_number("완료할 영상 ID: ")
    order, message = market.purchases.complete_lecture(student_id, course_id, lecture_id)
    print(message)
    print("현재 진도율:", market.purchases.get_progress_rate(student_id, course_id), "%")


def review_menu(market, current_user=None):
    print_line()
    print("[리뷰 작성]")
    if current_user is None:
        student_id = input_number("수강생 ID: ")
    else:
        student_id = current_user["id"]
    course_id = input_number("강의 ID: ")
    score = input_number("평점(1~5): ")
    content = input("리뷰 내용: ").strip()

    review, message = market.reviews.write_review(student_id, course_id, score, content)
    print(message)


def question_menu(market, current_user=None):
    print_line()
    print("[질문 등록]")
    if current_user is None:
        student_id = input_number("수강생 ID: ")
    else:
        student_id = current_user["id"]
    course_id = input_number("강의 ID: ")
    content = input("질문 내용: ").strip()

    question, message = market.questions.ask_question(student_id, course_id, content)
    print(message)
    if question is not None:
        print("질문 ID:", question["id"])


def answer_menu(market, current_user=None):
    print_line()
    print("[질문 답변]")
    if current_user is None:
        instructor_id = input_number("강사 ID: ")
    else:
        instructor_id = current_user["id"]
    question_id = input_number("질문 ID: ")
    answer = input("답변 내용: ").strip()

    question, message = market.questions.answer_question(instructor_id, question_id, answer)
    print(message)


def list_reviews(market):
    print_line()
    print("[리뷰 목록]")
    reviews = market.reviews.list_reviews()
    if len(reviews) == 0:
        print("등록된 리뷰가 없습니다.")
    for review in reviews:
        student = market.users.find_by_id(review["student_id"])
        course = market.courses.find_course(review["course_id"])
        student_name = "알 수 없음"
        course_title = "알 수 없음"
        if student is not None:
            student_name = student["name"]
        if course is not None:
            course_title = course["title"]
        print(
            review["id"],
            "수강생:",
            student_name,
            "강의:",
            course_title,
            "평점:",
            review["score"],
            "내용:",
            review["content"],
        )


def list_questions(market):
    print_line()
    print("[질문 목록]")
    questions = market.questions.list_questions()
    if len(questions) == 0:
        print("등록된 질문이 없습니다.")
    for question in questions:
        student = market.users.find_by_id(question["student_id"])
        course = market.courses.find_course(question["course_id"])
        student_name = "알 수 없음"
        course_title = "알 수 없음"
        if student is not None:
            student_name = student["name"]
        if course is not None:
            course_title = course["title"]
        answer_status = "답변완료"
        if question["answer"] == "":
            answer_status = "답변대기"
        print(
            question["id"],
            "수강생:",
            student_name,
            "강의:",
            course_title,
            "상태:",
            answer_status,
            "질문:",
            question["content"],
            "답변:",
            question["answer"],
        )


def print_guest_menu():
    print_line()
    print("온라인 강의 쇼핑몰 서비스")
    print("1. 회원 가입")
    print("2. 로그인")
    print("3. 전체 강의 목록")
    print("4. 승인된 강의 검색")
    print("0. 종료")


def print_student_menu(current_user):
    print_line()
    print("온라인 강의 쇼핑몰 서비스 - 수강생")
    print_current_user(current_user)
    print("1. 전체 강의 목록")
    print("2. 승인된 강의 검색")
    print("3. 강의 구매")
    print("4. 수강 완료")
    print("5. 리뷰 작성")
    print("6. 질문 등록")
    print("7. 리뷰 목록")
    print("8. 질문 목록")
    print("9. 구매 목록")
    print("10. 로그아웃")
    print("0. 종료")


def print_instructor_menu(current_user):
    print_line()
    print("온라인 강의 쇼핑몰 서비스 - 강사")
    print_current_user(current_user)
    print("1. 전체 강의 목록")
    print("2. 승인된 강의 검색")
    print("3. 강의 등록")
    print("4. 강의 영상 추가")
    print("5. 질문 목록")
    print("6. 질문 답변")
    print("7. 리뷰 목록")
    print("8. 로그아웃")
    print("0. 종료")


def print_admin_menu(current_user):
    print_line()
    print("온라인 강의 쇼핑몰 서비스 - 관리자")
    print_current_user(current_user)
    print("1. 회원 목록")
    print("2. 전체 강의 목록")
    print("3. 승인된 강의 검색")
    print("4. 강의 승인")
    print("5. 구매 목록")
    print("6. 리뷰 목록")
    print("7. 질문 목록")
    print("8. 로그아웃")
    print("0. 종료")


def main():
    market = MarketService()
    current_user = None

    while True:
        if current_user is None:
            print_guest_menu()
        elif current_user["role"] == "수강생":
            print_student_menu(current_user)
        elif current_user["role"] == "강사":
            print_instructor_menu(current_user)
        elif current_user["role"] == "관리자":
            print_admin_menu(current_user)

        choice = input("메뉴 선택: ")

        try:
            if choice == "0":
                print("프로그램을 종료합니다.")
                break

            if current_user is None:
                if choice == "1":
                    user_menu(market)
                elif choice == "2":
                    current_user = login_menu(market)
                elif choice == "3":
                    print_courses(market.courses.list_courses())
                elif choice == "4":
                    search_menu(market)
                else:
                    print("잘못된 메뉴입니다.")
            elif current_user["role"] == "수강생":
                if choice == "1":
                    print_courses(market.courses.list_courses())
                elif choice == "2":
                    search_menu(market)
                elif choice == "3":
                    buy_menu(market, current_user)
                elif choice == "4":
                    progress_menu(market, current_user)
                elif choice == "5":
                    review_menu(market, current_user)
                elif choice == "6":
                    question_menu(market, current_user)
                elif choice == "7":
                    list_reviews(market)
                elif choice == "8":
                    list_questions(market)
                elif choice == "9":
                    print_orders(market)
                elif choice == "10":
                    current_user = logout_menu()
                else:
                    print("잘못된 메뉴입니다.")
            elif current_user["role"] == "강사":
                if choice == "1":
                    print_courses(market.courses.list_courses())
                elif choice == "2":
                    search_menu(market)
                elif choice == "3":
                    course_menu(market, current_user)
                elif choice == "4":
                    lecture_menu(market, current_user)
                elif choice == "5":
                    list_questions(market)
                elif choice == "6":
                    answer_menu(market, current_user)
                elif choice == "7":
                    list_reviews(market)
                elif choice == "8":
                    current_user = logout_menu()
                else:
                    print("잘못된 메뉴입니다.")
            elif current_user["role"] == "관리자":
                if choice == "1":
                    print_users(market)
                elif choice == "2":
                    print_courses(market.courses.list_courses())
                elif choice == "3":
                    search_menu(market)
                elif choice == "4":
                    approve_menu(market, current_user)
                elif choice == "5":
                    print_orders(market)
                elif choice == "6":
                    list_reviews(market)
                elif choice == "7":
                    list_questions(market)
                elif choice == "8":
                    current_user = logout_menu()
                else:
                    print("잘못된 메뉴입니다.")
        except Exception as error:
            print("처리 중 오류가 발생했습니다:", clean_text(error))


main()
