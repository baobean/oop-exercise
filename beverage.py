class beverage:
    __name: str
    __price: float

    def __init__(self, name: str = "", price: float = 0) -> None:
        self.__name = name
        self.__price = price

    def update_name(self, new_name: str) -> None:
        self.__name = new_name

    def update_price(self, new_price: float) -> None:
        self.__price = new_price

    def display_info(self) -> None:
        print("Name:", self.__name)
        print("Price:", self.__price)