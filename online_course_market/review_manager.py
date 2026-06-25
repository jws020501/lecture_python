from base_manager import BaseManager
from validation import clean_text, score_value, to_int


class ReviewManager(BaseManager):
    def write_review(self, student_id, course_id, score, content):
        student_id = to_int(student_id)
        course_id = to_int(course_id)
        content = clean_text(content)
        score = score_value(score)
        if content == "":
            return None, "리뷰 내용은 비워둘 수 없습니다."
        if self.find_order(student_id, course_id) is None:
            return None, "구매자만 리뷰를 작성할 수 있습니다."
        if score is None:
            return None, "평점은 1점부터 5점까지 입력해야 합니다."
        if self.find_review(student_id, course_id) is not None:
            return None, "이미 이 강의에 리뷰를 작성했습니다."

        review = {
            "id": self.store.review_id,
            "student_id": student_id,
            "course_id": course_id,
            "score": score,
            "content": content,
        }
        self.store.reviews.append(review)
        self.store.review_id = self.store.review_id + 1
        self.store.save()
        return review, "리뷰가 등록되었습니다."

    def list_reviews(self):
        return self.store.reviews

    def find_review(self, student_id, course_id):
        student_id = to_int(student_id)
        course_id = to_int(course_id)
        for review in self.store.reviews:
            if (
                to_int(review.get("student_id")) == student_id
                and to_int(review.get("course_id")) == course_id
            ):
                return review
        return None
