from validation import to_int


class BaseManager:
    def __init__(self, store):
        self.store = store

    def find_user(self, user_id):
        user_id = to_int(user_id)
        for user in self.store.users:
            if to_int(user.get("id")) == user_id:
                return user
        return None

    def find_course(self, course_id):
        course_id = to_int(course_id)
        for course in self.store.courses:
            if to_int(course.get("id")) == course_id:
                return course
        return None

    def find_order(self, student_id, course_id):
        student_id = to_int(student_id)
        course_id = to_int(course_id)
        for order in self.store.orders:
            if (
                to_int(order.get("student_id")) == student_id
                and to_int(order.get("course_id")) == course_id
            ):
                return order
        return None
