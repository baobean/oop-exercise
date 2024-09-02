import book
import beverage

class cafe:
    def __init__(self) -> None:
        self.books = []
        self.beverages = []

    def add_books(self, book: book.book) -> None:
        self.books.append(book)

    def remove_book(self, book: book.book) -> None:
        self.books.remove(book)

    def add_beverage(self, beverage: beverage.beverage) -> None:
        self.beverages.append(beverage)

    def remove_beverage(self, beverage: beverage.beverage) -> None:
        self.beverages.remove(beverage)

    def display_books(self) -> None:
        print("List of books in the cafe:")
        for book in self.books:
            print("----------")
            book.display_info()
        print("\n")

    def display_beverages(self) -> None:
        print("List of beverages in the cafe:")
        for beverage in self.beverages:
            print("----------")
            beverage.display_info()
        print("\n")