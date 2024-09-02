import book
import beverage
import cafe

shop = cafe.cafe()

book1 = book.book("Hamlet", "William Shakespeare", "This is a play", 2.82)
book2 = book.book("The Call of the Wild", "Jack London", "Story about a dog", 6.02)
book3 = book.book("Les Miserables", "Victor Hugo", "This book is written in France", 5.99)

bev1 = beverage.beverage("Americano", 1.15)
bev2 = beverage.beverage("Hot Chocolate", 1.07)
bev3 = beverage.beverage("Green Tea", 1.02)

shop.add_books(book1)
shop.add_books(book2)
shop.add_books(book3)

shop.add_beverage(bev1)
shop.add_beverage(bev2)
shop.add_beverage(bev3)

shop.display_books()
shop.display_beverages()

shop.books[0].update_title("Romeo and Juliet")
shop.books[0].update_abstract("None")
shop.beverages[1].update_name("Cappuccino")
shop.beverages[1].update_price(0.0123)

shop.books[0].display_info()
print("----------")
shop.beverages[1].display_info()