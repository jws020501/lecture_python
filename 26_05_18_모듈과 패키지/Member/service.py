from .models import Member


class MemberService:
    def __init__(self):
        self.__member_list = []

    def member_sign(self, member_no, member_id, pw, name, call_no, address):
        member = Member(member_no, member_id, pw, name, call_no, address)
        self.__member_list.append(member)
        return True
    
    def list_member(self):
        return self.__member_list

    def member_detail(self, member_id):
        for member in self.__member_list:
            if member.get_member_id() == member_id:
                return member
        return None

    def member_edit(self, member_id, new_pw, new_name, new_call_no, new_address):
        member = self.member_detail(member_id)
        if member:
            member.set_pw(new_pw)
            member.set_name(new_name)
            member.set_call_no(new_call_no)
            member.set_address(new_address)
            return True
        return False

    def member_del(self, member_id):
        member = self.member_detail(member_id)
        if member:
            self.__member_list.remove(member)
            return True
        return False
