import joblib
import os

class BookDAO:
    BOOK_DB_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'db', 'bookDB.pkl')

    def __init__(self):
        self.__bookDB = self.__load_bookDB()

    def __load_bookDB(self):
        try:
            data = joblib.load(BookDAO.BOOK_DB_FILE)
            if data is None or not isinstance(data, dict):
                return {}
            return data
        except Exception:
            return {}

    def save_bookDB(self):
        if self.__bookDB is None:
            self.__bookDB = {}
            
        try:
            joblib.dump(self.__bookDB, BookDAO.BOOK_DB_FILE)
        except Exception:
            pass

    def insert_book(self, book):
        if self.is_exist(book.get_book_id()):
            return False
        self.__bookDB[book.get_book_id()] = book
        self.save_bookDB()
        return True

    def is_exist(self, book_id):
        if self.__bookDB is None:
            self.__bookDB = {}
            return False
        return book_id in self.__bookDB

    def get_all_books(self):
        if not self.__bookDB:
            return []
        return list(self.__bookDB.values())
    def get_book_info(self, book_id):
        if not self.__bookDB:
            return None
        try:
            target_id = int(book_id)
            if target_id in self.__bookDB:
                return self.__bookDB[target_id]
        except (ValueError, TypeError):
            pass
        return None
    def update_book(self, book):
        if not self.__bookDB or not book:
            return False
        book_id = book.get_book_id()
        if book_id in self.__bookDB:
            self.__bookDB[book_id] = book
            self.save_bookDB()
            return True
        return False

    def delete_book(self, book_id):
        if not self.__bookDB:
            return False
        try:
            target_id = int(book_id)
        except (ValueError, TypeError):
            return False
        if target_id in self.__bookDB:
            del self.__bookDB[target_id]
            self.save_bookDB()
            return True
        return False
