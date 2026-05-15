try:
    from memberDto import Member
except ImportError:
    from .memberDto import Member


NOT_FOUND_MSG = "결과 : 일치하는 회원이 없습니다."


class MemberService:
    def __init__(self):
        self.members = []
        self.next_no = 1

    def member_sign(self, member_no, member_id, pw, name, call_no, address):
        if self.member_detail(member_id) is not None:
            print("결과 : 이미 사용 중인 아이디입니다.")
            return False

        member = Member(member_no, member_id, pw, name, call_no, address)
        self.members.append(member)
        return True

    def list_member(self):
        return self.members[:]

    def member_detail(self, member_id):
        for member in self.members:
            if member.get_member_id() == member_id:
                return member
        return None

    def member_del(self, member_id):
        member = self.member_detail(member_id)
        if member is None:
            return False
        self.members.remove(member)
        return True

    def member_edit(self, member_id, pw=None, name=None, call_no=None, address=None):
        member = self.member_detail(member_id)
        if member is None:
            return False

        if pw is not None:
            member.pw = pw
        if name is not None:
            member.name = name
        if call_no is not None:
            member.call_no = call_no
        if address is not None:
            member.address = address

        return True


def select_menu():
    print("=================================================================================")
    print(" 1. 회원가입 | 2. 회원목록 | 3. 회원상세정보 | 4. 회원정보수정 | 5. 회원탈퇴 | 0.종료")
    print("=================================================================================")
    menu = int(input(">> 메뉴 선택 : "))
    return menu


if __name__ == "__main__":
    mservice = MemberService()

    print()
    print(" =========== MEMBER ===========")
    while True:
        menu = select_menu()
        if menu == 0:
            break

        elif menu == 1:
            member_no = input("> 회원번호 : ")
            member_id = input("> 아이디 : ")
            pw = input("> 비밀번호 : ")
            name = input("> 이름 : ")
            call_no = input("> 전화번호 : ")
            address = input("> 주소 : ")

            if mservice.member_sign(member_no, member_id, pw, name, call_no, address):
                print("결과 : 회원가입이 완료 되었습니다.")

        elif menu == 2:
            member_list = mservice.list_member()
            print("-------------")
            print(" 회원목록")
            print("-------------")
            if not member_list:
                print("등록된 회원정보가 없습니다")
            else:
                for member in member_list:
                    print(f"- {member.get_member_id()}")

        elif menu == 3:
            print("-------------")
            print(" 회원상세정보")
            print("-------------")
            member_id = input("> 조회할 아이디 : ")
            member = mservice.member_detail(member_id)
            if member:
                print(f"회원번호 : {member.get_member_no()}")
                print(f"아이디   : {member.get_member_id()}")
                print(f"비밀번호 : {member.get_pw()}")
                print(f"이름     : {member.get_name()}")
                print(f"전화번호 : {member.get_call_no()}")
                print(f"주소     : {member.get_address()}")
            else:
                print(NOT_FOUND_MSG)

        elif menu == 4:
            print("-------------")
            print(" 회원정보수정")
            print("-------------")
            member_id = input("> 수정할 아이디 : ")

            if mservice.member_detail(member_id):
                new_pw = input("> 새 비밀번호 : ")
                new_name = input("> 새 이름 : ")
                new_call_no = input("> 새 전화번호 : ")
                new_address = input("> 새 주소 : ")

                if mservice.member_edit(member_id, new_pw, new_name, new_call_no, new_address):
                    print("결과 : 회원 정보가 수정되었습니다.")
            else:
                print(NOT_FOUND_MSG)

        elif menu == 5:
            print("-------------")
            print(" 회원탈퇴")
            print("-------------")
            member_id = input("> 탈퇴할 아이디 : ")
            if mservice.member_del(member_id):
                print("결과 : 회원 탈퇴가 완료되었습니다.")
            else:
                print(NOT_FOUND_MSG)
