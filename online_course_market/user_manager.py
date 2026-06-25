from base_manager import BaseManager
from validation import clean_text


class UserManager(BaseManager):
    VALID_ROLES = ["관리자", "강사", "수강생"]

    def create_user(self, name, role, login_id="", password="", phone="", email=""):
        name = clean_text(name)
        role = clean_text(role)
        login_id = clean_text(login_id)
        password = clean_text(password)
        phone = clean_text(phone)
        email = clean_text(email)

        if name == "":
            return None
        if role not in self.VALID_ROLES:
            return None
        if login_id == "":
            login_id = "user" + str(self.store.user_id)
        if self.is_login_id_used(login_id):
            return None
        if password == "":
            password = "1234"

        user = {
            "id": self.store.user_id,
            "login_id": login_id,
            "password": password,
            "name": name,
            "role": role,
            "phone": phone,
            "email": email,
        }
        self.store.users.append(user)
        self.store.user_id = self.store.user_id + 1
        self.store.save()
        return user

    def list_users(self):
        return self.store.users

    def find_by_login_id(self, login_id):
        login_id = clean_text(login_id)
        for user in self.store.users:
            if user.get("login_id") == login_id:
                return user
        return None

    def find_by_id(self, user_id):
        return self.find_user(user_id)

    def is_login_id_used(self, login_id):
        user = self.find_by_login_id(login_id)
        if user is None:
            return False
        return True

    def login(self, login_id, password):
        password = clean_text(password)
        user = self.find_by_login_id(login_id)
        if user is None:
            return None, "아이디가 존재하지 않습니다."
        if user.get("password") != password:
            return None, "비밀번호가 올바르지 않습니다."
        return user, "로그인되었습니다."
