import json
from pathlib import Path
from json import JSONDecodeError

from validation import to_int


class MarketStore:
    def __init__(self, data_path=None):
        if data_path is None:
            data_path = Path(__file__).parent / "data" / "market_store.json"
        self.data_path = Path(data_path)

        self.user_id = 1
        self.course_id = 1
        self.lecture_id = 1
        self.order_id = 1
        self.review_id = 1
        self.question_id = 1
        self.users = []
        self.courses = []
        self.orders = []
        self.reviews = []
        self.questions = []

        self.load()

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "course_id": self.course_id,
            "lecture_id": self.lecture_id,
            "order_id": self.order_id,
            "review_id": self.review_id,
            "question_id": self.question_id,
            "users": self.users,
            "courses": self.courses,
            "orders": self.orders,
            "reviews": self.reviews,
            "questions": self.questions,
        }

    def load(self):
        if not self.data_path.exists():
            self.add_sample_data()
            self.save()
            return

        try:
            with self.data_path.open("r", encoding="utf-8") as file:
                data = json.load(file)
        except (OSError, JSONDecodeError):
            self._backup_broken_data()
            self.add_sample_data()
            self.save()
            return

        if not isinstance(data, dict):
            self._backup_broken_data()
            self.add_sample_data()
            self.save()
            return

        self.user_id = max(1, to_int(data.get("user_id"), 1))
        self.course_id = max(1, to_int(data.get("course_id"), 1))
        self.lecture_id = max(1, to_int(data.get("lecture_id"), 1))
        self.order_id = max(1, to_int(data.get("order_id"), 1))
        self.review_id = max(1, to_int(data.get("review_id"), 1))
        self.question_id = max(1, to_int(data.get("question_id"), 1))
        self.users = self._list_of_dicts(data.get("users"))
        self.courses = self._list_of_dicts(data.get("courses"))
        self.orders = self._list_of_dicts(data.get("orders"))
        self.reviews = self._list_of_dicts(data.get("reviews"))
        self.questions = self._list_of_dicts(data.get("questions"))
        self._restore_progress_keys()
        self._fill_missing_user_fields()

        if len(self.users) == 0 and len(self.courses) == 0:
            self.add_sample_data()
            self.save()

    def save(self):
        self.data_path.parent.mkdir(parents=True, exist_ok=True)
        temp_path = self.data_path.with_suffix(self.data_path.suffix + ".tmp")
        with temp_path.open("w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file, ensure_ascii=False, indent=2)
        temp_path.replace(self.data_path)

    def _backup_broken_data(self):
        if not self.data_path.exists():
            return
        backup_path = self.data_path.with_suffix(self.data_path.suffix + ".broken")
        try:
            self.data_path.replace(backup_path)
        except OSError:
            pass

    def _list_of_dicts(self, value):
        if not isinstance(value, list):
            return []
        return [item for item in value if isinstance(item, dict)]

    def _restore_progress_keys(self):
        for order in self.orders:
            progress = order.get("progress", {})
            if not isinstance(progress, dict):
                progress = {}
            restored = {}
            for lecture_id, value in progress.items():
                lecture_id = to_int(lecture_id)
                if lecture_id > 0:
                    restored[lecture_id] = bool(value)
            order["progress"] = restored

    def _fill_missing_user_fields(self):
        for user in self.users:
            user_id = to_int(user.get("id"), self.user_id)
            user["id"] = user_id
            user.setdefault("login_id", "user" + str(user_id))
            user.setdefault("password", "1234")
            user.setdefault("name", "이름없음")
            user.setdefault("role", "수강생")
            user.setdefault("phone", "")
            user.setdefault("email", "")

    def add_sample_data(self):
        self.users = [
            {
                "id": 1,
                "login_id": "admin",
                "password": "admin1234",
                "name": "관리자",
                "role": "관리자",
                "phone": "010-0000-0000",
                "email": "admin@market.com",
            },
            {
                "id": 2,
                "login_id": "teacher",
                "password": "teacher1234",
                "name": "김강사",
                "role": "강사",
                "phone": "010-1111-2222",
                "email": "teacher@market.com",
            },
            {
                "id": 3,
                "login_id": "student",
                "password": "student1234",
                "name": "이수강",
                "role": "수강생",
                "phone": "010-3333-4444",
                "email": "student@market.com",
            },
        ]
        self.courses = [
            {
                "id": 1,
                "title": "파이썬 기초 문법",
                "category": "프로그래밍",
                "price": 30000,
                "instructor_id": 2,
                "status": "승인완료",
                "lectures": [
                    {"id": 1, "title": "변수와 자료형"},
                    {"id": 2, "title": "조건문과 반복문"},
                ],
            },
            {
                "id": 2,
                "title": "콘솔 쇼핑몰 만들기",
                "category": "프로젝트",
                "price": 45000,
                "instructor_id": 2,
                "status": "승인완료",
                "lectures": [
                    {"id": 3, "title": "메뉴 설계"},
                    {"id": 4, "title": "파일 저장 구현"},
                ],
            },
            {
                "id": 3,
                "title": "자료구조 입문",
                "category": "컴퓨터공학",
                "price": 40000,
                "instructor_id": 2,
                "status": "승인대기",
                "lectures": [
                    {"id": 5, "title": "리스트와 딕셔너리"},
                ],
            },
        ]
        self.orders = []
        self.reviews = []
        self.questions = []
        self.user_id = 4
        self.course_id = 4
        self.lecture_id = 6
        self.order_id = 1
        self.review_id = 1
        self.question_id = 1
