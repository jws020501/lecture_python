class CartItem:
    def __init__(self, book, quantity):
        self.__book = book
        self.__quantity = quantity

    def get_book(self): return self.__book
    def get_quantity(self): return self.__quantity
    
    def set_quantity(self, quantity): self.__quantity = quantity