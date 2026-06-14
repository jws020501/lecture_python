class Member:
    def __init__(self, id, password, name, address="", order_list=None):
        self.__id = id
        self.__password = password
        self.__name = name
        self.__address = address
        self.__cart = []  
        self.__order_list = order_list if order_list is not None else []  

    def get_id(self): return self.__id
    def get_password(self): return self.__password
    def get_name(self): return self.__name
    def get_address(self): return self.__address
    def get_cart(self): return self.__cart
    def get_order_list(self): return self.__order_list
    
    def set_password(self, password): self.__password = password
    def set_address(self, address): self.__address = address
    def clear_cart(self): self.__cart = []

    def __str__(self):
        return f'ID: {self.__id}\t| 이름: {self.__name}\t| 주소: {self.__address}\t| 주문건수: {len(self.__order_list)}건'