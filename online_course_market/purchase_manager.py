from base_manager import BaseManager
from validation import to_int


class PurchaseManager(BaseManager):
    def buy_course(self, student_id, course_id):
        student_id = to_int(student_id)
        course_id = to_int(course_id)
        student = self.find_user(student_id)
        if student is None:
            return None, "수강생을 찾을 수 없습니다."
        if student.get("role") != "수강생":
            return None, "수강생만 강의를 구매할 수 있습니다."

        course = self.find_course(course_id)
        if course is None:
            return None, "강의를 찾을 수 없습니다."
        if course.get("status") != "승인완료":
            return None, "승인된 강의만 구매할 수 있습니다."
        if self.find_order(student_id, course_id) is not None:
            return None, "이미 구매한 강의입니다."

        progress = {}
        for lecture in course.get("lectures", []):
            lecture_id = to_int(lecture.get("id"))
            if lecture_id > 0:
                progress[lecture_id] = False

        order = {
            "id": self.store.order_id,
            "student_id": student_id,
            "course_id": course_id,
            "price": course.get("price", 0),
            "progress": progress,
        }
        self.store.orders.append(order)
        self.store.order_id = self.store.order_id + 1
        self.store.save()
        return order, "강의를 구매했습니다."

    def complete_lecture(self, student_id, course_id, lecture_id):
        lecture_id = to_int(lecture_id)
        order = self.find_order(student_id, course_id)
        if order is None:
            return None, "구매한 강의만 수강할 수 있습니다."
        if lecture_id not in order["progress"]:
            return None, "해당 강의에 없는 영상입니다."

        order["progress"][lecture_id] = True
        self.store.save()
        return order, "수강 완료 처리되었습니다."

    def get_progress_rate(self, student_id, course_id):
        order = self.find_order(student_id, course_id)
        if order is None:
            return 0

        total = len(order["progress"])
        if total == 0:
            return 0

        completed = 0
        for lecture_id in order["progress"]:
            if order["progress"][lecture_id] is True:
                completed = completed + 1
        return int(completed / total * 100)

    def list_orders(self):
        return self.store.orders
