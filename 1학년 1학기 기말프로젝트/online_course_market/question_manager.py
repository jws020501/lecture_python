from base_manager import BaseManager
from validation import clean_text, to_int


class QuestionManager(BaseManager):
    def ask_question(self, student_id, course_id, content):
        student_id = to_int(student_id)
        course_id = to_int(course_id)
        content = clean_text(content)
        if content == "":
            return None, "질문 내용은 비워둘 수 없습니다."
        if self.find_order(student_id, course_id) is None:
            return None, "구매자만 질문할 수 있습니다."

        question = {
            "id": self.store.question_id,
            "student_id": student_id,
            "course_id": course_id,
            "content": content,
            "answer": "",
        }
        self.store.questions.append(question)
        self.store.question_id = self.store.question_id + 1
        self.store.save()
        return question, "질문이 등록되었습니다."

    def answer_question(self, instructor_id, question_id, answer):
        instructor_id = to_int(instructor_id)
        answer = clean_text(answer)
        if answer == "":
            return None, "답변 내용은 비워둘 수 없습니다."

        question = None
        question_id = to_int(question_id)
        for item in self.store.questions:
            if to_int(item.get("id")) == question_id:
                question = item

        if question is None:
            return None, "질문을 찾을 수 없습니다."

        course = self.find_course(question.get("course_id"))
        if course is None:
            return None, "질문과 연결된 강의를 찾을 수 없습니다."
        if to_int(course.get("instructor_id")) != instructor_id:
            return None, "담당 강사만 답변할 수 있습니다."

        question["answer"] = answer
        self.store.save()
        return question, "답변이 등록되었습니다."

    def list_questions(self):
        return self.store.questions
