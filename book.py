class book:
    __title: str
    __author: str
    __abstract: str
    __price_to_loan: float

    def __init__(self, title: str = "", author: str = "", abstract: str = "", price_to_loan: float = 0) -> None:
        self.__title = title
        self.__author = author
        self.__abstract = abstract
        self.__price_to_loan = price_to_loan

    def update_title(self, new_title: str) -> None:
        self.__title = new_title

    def update_author(self, new_author: str) -> None:
        self.__author = new_author

    def update_abstract(self, new_abstract: str) -> None:
        self.__abstract = new_abstract

    def update_price(self, new_price: float) -> None:
        self.__price_to_loan = new_price

    def display_info(self) -> None:
        print("Title:", self.__title)
        print("Author:", self.__author)
        print("Abstract:", self.__abstract)
        print("Price to loan:", self.__price_to_loan)