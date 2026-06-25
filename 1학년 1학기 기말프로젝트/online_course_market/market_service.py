from store import MarketStore
from user_manager import UserManager
from course_manager import CourseManager
from purchase_manager import PurchaseManager
from review_manager import ReviewManager
from question_manager import QuestionManager


class MarketService:
    def __init__(self, data_path=None):
        self.store = MarketStore(data_path)
        self.users = UserManager(self.store)
        self.courses = CourseManager(self.store)
        self.purchases = PurchaseManager(self.store)
        self.reviews = ReviewManager(self.store)
        self.questions = QuestionManager(self.store)
