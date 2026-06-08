import json
import os
from member.member import Member


class MemberDAO:
    def __init__(self):
        self.__file_path = 'data/members.json'
        self.__member_db = self.__load()

    def __load(self):
        if not os.path.exists(self.__file_path):
            return {}

        with open(self.__file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        result = {}

        for id, member_data in data.items():
            result[id] = Member.from_dict(member_data)

        return result

    def __save(self):
        data = {}

        for id, member in self.__member_db.items():
            data[id] = member.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def insert_member(self, member):
        self.__member_db[member.get_id()] = member
        self.__save()
        return True

    def select_member(self, id):
        return self.__member_db.get(id)

    def select_all_member(self):
        return list(self.__member_db.values())

    def update_member(self, member):
        self.__member_db[member.get_id()] = member
        self.__save()
        return True

    def delete_member(self, id):
        if id in self.__member_db:
            del self.__member_db[id]
            self.__save()
            return True

        return False