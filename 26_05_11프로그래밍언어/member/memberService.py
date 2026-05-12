try:
    from memberDto import Member
except ImportError:
    from .memberDto import Member


class MemberService:
    def __init__(self):
        self.members = []
        self.next_no = 1

    def add_member(self, member_id, pw, name, phone, adress):
        if self.find_by_id(member_id) is not None:
            raise ValueError("이미 사용 중인 아이디입니다.")

        member = Member(self.next_no, member_id, pw, name, phone, adress)
        self.members.append(member)
        self.next_no += 1
        return member

    def list_members(self):
        return self.members[:]

    def find_by_id(self, member_id):
        for member in self.members:
            if member.id == member_id:
                return member
        return None

    def remove_member(self, member_id):
        member = self.find_by_id(member_id)
        if member is None:
            return False
        self.members.remove(member)
        return True

    def get_member_detail(self, member_id):
        return self.find_by_id(member_id)

    def update_member(self, member_id, pw=None, name=None, phone=None, adress=None):
        member = self.find_by_id(member_id)
        if member is None:
            return False

        if pw is not None:
            member.pw = pw
        if name is not None:
            member.name = name
        if phone is not None:
            member.phone = phone
        if adress is not None:
            member.adress = adress

        return True