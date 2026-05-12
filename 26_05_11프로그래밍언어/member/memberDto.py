class Member:
    def __init__(self, no, member_id, pw, name, phone, adress):
        self.no = no
        self.id = member_id
        self.pw = pw
        self.name = name
        self.phone = phone
        self.adress = adress

    def to_dict(self):
        return {
            "no": self.no,
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "adress": self.adress,
        }

    def __str__(self):
        return (
            f"회원번호: {self.no}, 아이디: {self.id}, 이름: {self.name}, "
            f"전화번호: {self.phone}, 주소: {self.adress}"
        )
    