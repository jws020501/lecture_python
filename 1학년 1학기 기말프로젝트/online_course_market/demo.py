from market_service import MarketService


def main():
    market = MarketService()

    admin = market.users.create_user("관리자", "관리자")
    instructor = market.users.create_user("김강사", "강사")
    student = market.users.create_user("이수강", "수강생")

    course, message = market.courses.create_course(
        instructor["id"],
        "파이썬 기초",
        "프로그래밍",
        30000,
    )
    print(message)

    lecture, message = market.courses.add_lecture(
        instructor["id"],
        course["id"],
        "변수와 조건문",
    )
    print(message)

    course, message = market.courses.approve_course(admin["id"], course["id"])
    print(message)

    order, message = market.purchases.buy_course(student["id"], course["id"])
    print(message)

    order, message = market.purchases.complete_lecture(
        student["id"],
        course["id"],
        lecture["id"],
    )
    print(message)

    review, message = market.reviews.write_review(
        student["id"],
        course["id"],
        5,
        "설명이 쉽습니다.",
    )
    print(message)

    question, message = market.questions.ask_question(
        student["id"],
        course["id"],
        "반복문은 언제 쓰나요?",
    )
    print(message)

    question, message = market.questions.answer_question(
        instructor["id"],
        question["id"],
        "같은 작업을 여러 번 반복할 때 사용합니다.",
    )
    print(message)

    print("구매 강의:", course["title"])
    print("진도율:", market.purchases.get_progress_rate(student["id"], course["id"]), "%")
    print("질문 답변:", question["answer"])


main()
