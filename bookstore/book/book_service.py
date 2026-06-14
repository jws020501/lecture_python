from book.book_dao import BookDAO
from book.book import Book


class BookService:
    def __init__(self, bookDAO):
        self.__DAO = bookDAO

    def insert_book(self, book):
        return self.__DAO.insert_book(book)

    def get_book_list(self):
        return self.__DAO.get_all_books()

    def get_book_info(self, book_id):
        return self.__DAO.get_book_info(book_id)

    def update_book_info(self, book):
        return self.__DAO.update_book(book)

    def remove_book(self, book_id):
        return self.__DAO.delete_book(book_id)