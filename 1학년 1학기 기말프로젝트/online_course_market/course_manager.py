from base_manager import BaseManager
from validation import clean_text, positive_int, to_int


class CourseManager(BaseManager):
    def create_course(self, instructor_id, title, category, price):
        instructor_id = to_int(instructor_id)
        title = clean_text(title)
        category = clean_text(category)
        price = positive_int(price)
        if title == "":
            return None, "강의명은 비워둘 수 없습니다."
        if category == "":
            return None, "카테고리는 비워둘 수 없습니다."
        if price is None:
            return None, "가격은 0원보다 커야 합니다."

        instructor = self.find_user(instructor_id)
        if instructor is None:
            return None, "강사를 찾을 수 없습니다."
        if instructor.get("role") != "강사":
            return None, "강사만 강의를 등록할 수 있습니다."

        course = {
            "id": self.store.course_id,
            "title": title,
            "category": category,
            "price": price,
            "instructor_id": instructor_id,
            "status": "승인대기",
            "lectures": [],
        }
        self.store.courses.append(course)
        self.store.course_id = self.store.course_id + 1
        self.store.save()
        return course, "강의가 등록되었습니다."

    def add_lecture(self, instructor_id, course_id, title):
        instructor_id = to_int(instructor_id)
        title = clean_text(title)
        if title == "":
            return None, "영상 제목은 비워둘 수 없습니다."

        course = self.find_course(course_id)
        if course is None:
            return None, "강의를 찾을 수 없습니다."
        if to_int(course.get("instructor_id")) != instructor_id:
            return None, "본인 강의에만 영상을 추가할 수 있습니다."

        lecture = {
            "id": self.store.lecture_id,
            "title": title,
        }
        course.setdefault("lectures", [])
        course["lectures"].append(lecture)
        message = "강의 영상이 추가되었습니다."
        if course["status"] == "승인완료":
            course["status"] = "승인대기"
            message = "강의 영상이 추가되었습니다. 승인대기 상태로 변경되었습니다."
        self.store.lecture_id = self.store.lecture_id + 1
        self.store.save()
        return lecture, message

    def approve_course(self, admin_id, course_id):
        admin_id = to_int(admin_id)
        admin = self.find_user(admin_id)
        if admin is None:
            return None, "관리자를 찾을 수 없습니다."
        if admin.get("role") != "관리자":
            return None, "관리자만 강의를 승인할 수 있습니다."

        course = self.find_course(course_id)
        if course is None:
            return None, "강의를 찾을 수 없습니다."
        if len(course.get("lectures", [])) == 0:
            return None, "영상이 1개 이상 있어야 승인할 수 있습니다."

        course["status"] = "승인완료"
        self.store.save()
        return course, "강의가 승인되었습니다."

    def list_courses(self):
        return self.store.courses

    def list_approved_courses(self):
        result = []
        for course in self.store.courses:
            if course.get("status") == "승인완료":
                result.append(course)
        return result

    def search_courses(self, keyword):
        keyword = clean_text(keyword).lower()
        result = []
        for course in self.store.courses:
            instructor = self.find_user(course.get("instructor_id"))
            instructor_name = ""
            if instructor is not None:
                instructor_name = instructor.get("name", "")

            title = course.get("title", "").lower()
            category = course.get("category", "").lower()
            instructor_name = instructor_name.lower()

            if (
                course.get("status") == "승인완료"
                and (
                    keyword == ""
                    or keyword in title
                    or keyword in category
                    or keyword in instructor_name
                )
            ):
                result.append(course)
        return result
