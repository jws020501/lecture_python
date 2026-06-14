import joblib
import os

class MemberDAO:
    MEMBER_DB_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'db', 'memberDB.pkl')
    
    def __init__(self):
        self.__memberDB = self.__load_memberDB()
        
        if self.__memberDB is None or not isinstance(self.__memberDB, list):
            self.__memberDB = []

    def __load_memberDB(self):
        try:
            data = joblib.load(MemberDAO.MEMBER_DB_FILE)
            if data is None or not isinstance(data, list):
                return []
            return data
        except Exception:
            return []
        
    def save_memberDB(self):
        if self.__memberDB is None:
            self.__memberDB = []
        try:
            joblib.dump(self.__memberDB, MemberDAO.MEMBER_DB_FILE)
        except Exception:
            pass

    def update_memberDB(self):
        self.save_memberDB()
        self.__memberDB = self.__load_memberDB()

    def insert_member(self, member):
        if self.is_exist(member.get_id()):
            return False
        self.__memberDB.append(member)
        self.save_memberDB()  
        return True

    def is_exist(self, id):
        if self.__memberDB is None:
            self.__memberDB = []
        
        for member in self.__memberDB:
            if member.get_id() == id:
                return True
        return False

    def get_member_info(self, id):
        if not self.__memberDB:
            return None
        for member in self.__memberDB:
            if member.get_id() == id:
                return member
        return None

    def get_all_members(self):
        if self.__memberDB is None:
            return []
        return self.__memberDB

    def delete_member(self, id):
        if not self.__memberDB:
            return False
        for idx, member in enumerate(self.__memberDB):
            if member.get_id() == id:
                del self.__memberDB[idx]
                self.save_memberDB()  
                return True
        return False

    def update_member_address(self, id, new_address):
        member = self.get_member_info(id)
        if member:
            member.set_address(new_address)
            self.save_memberDB()
            return True
        return False

    def update_member_password(self, id, org_password, new_password):
        member = self.get_member_info(id)
        if member and member.get_password() == org_password:
            member.set_password(new_password)
            self.save_memberDB()
            return True
        return False