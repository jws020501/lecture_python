import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from market_service import MarketService


class MarketServiceTest(unittest.TestCase):
    def make_market(self):
        temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(temp_dir.cleanup)
        return MarketService(Path(temp_dir.name) / "market_store.json")

    def test_full_course_flow(self):
        market = self.make_market()

        course, message = market.courses.create_course(2, "  Django 입문  ", "웹", "25000")
        self.assertEqual(message, "강의가 등록되었습니다.")
        self.assertIsNotNone(course)

        lecture, message = market.courses.add_lecture("2", course["id"], "설치")
        self.assertEqual(message, "강의 영상이 추가되었습니다.")
        self.assertIsNotNone(lecture)

        course, message = market.courses.approve_course(1, course["id"])
        self.assertEqual(message, "강의가 승인되었습니다.")

        order, message = market.purchases.buy_course(3, course["id"])
        self.assertEqual(message, "강의를 구매했습니다.")
        self.assertIsNotNone(order)

        order, message = market.purchases.complete_lecture(3, course["id"], lecture["id"])
        self.assertEqual(message, "수강 완료 처리되었습니다.")
        self.assertEqual(market.purchases.get_progress_rate(3, course["id"]), 100)

        review, message = market.reviews.write_review(3, course["id"], "5", "좋아요")
        self.assertEqual(message, "리뷰가 등록되었습니다.")
        self.assertIsNotNone(review)

        question, message = market.questions.ask_question(3, course["id"], "자료 어디 있나요?")
        self.assertEqual(message, "질문이 등록되었습니다.")
        self.assertIsNotNone(question)

        question, message = market.questions.answer_question(2, question["id"], "강의 자료실에 있습니다.")
        self.assertEqual(message, "답변이 등록되었습니다.")
        self.assertEqual(question["answer"], "강의 자료실에 있습니다.")

    def test_invalid_inputs_return_messages_without_crashing(self):
        market = self.make_market()

        user = market.users.create_user(None, "수강생")
        self.assertIsNone(user)

        course, message = market.courses.create_course(2, "강의", "카테고리", "무료")
        self.assertIsNone(course)
        self.assertEqual(message, "가격은 0원보다 커야 합니다.")

        market.purchases.buy_course(3, 1)
        lecture, message = market.purchases.complete_lecture(3, 1, "abc")
        self.assertIsNone(lecture)
        self.assertEqual(message, "해당 강의에 없는 영상입니다.")

        review, message = market.reviews.write_review(3, 1, "별다섯", "내용")
        self.assertIsNone(review)
        self.assertEqual(message, "평점은 1점부터 5점까지 입력해야 합니다.")

        question, message = market.questions.answer_question(2, "없는질문", None)
        self.assertIsNone(question)
        self.assertEqual(message, "답변 내용은 비워둘 수 없습니다.")

    def test_corrupt_json_is_backed_up_and_sample_data_restored(self):
        temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(temp_dir.cleanup)
        data_path = Path(temp_dir.name) / "market_store.json"
        data_path.write_text("{ broken json", encoding="utf-8")

        market = MarketService(data_path)

        self.assertTrue(data_path.exists())
        self.assertTrue(data_path.with_suffix(".json.broken").exists())
        self.assertGreaterEqual(len(market.users.list_users()), 3)

        with data_path.open("r", encoding="utf-8") as file:
            restored = json.load(file)
        self.assertIn("users", restored)


if __name__ == "__main__":
    unittest.main()
