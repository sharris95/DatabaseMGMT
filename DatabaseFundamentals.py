#Database Fundamentals Python
class Author:
    def __init__(self, author_id, name, biography):
        self.author_id = author_id
        self.name = name
        self.biography = biography
        self.books = []

    def add_book(self, book):
        self.books.append(book)

class Book:
    def __init__(self, book_id, title, author, genre, price, publication_date):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.publication_date = publication_date
        self.available = True

class Customer:
    def __init__(self, customer_id, name, email, phone):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            self.borrowed_books.append(book)
            book.available = False
        else:
            print(f"The book '{book.title}' is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.available = True

class Transaction:
    def __init__(self, transaction_id, book, customer, transaction_date, quantity, total_price):
        self.transaction_id = transaction_id
        self.book = book
        self.customer = customer
        self.transaction_date = transaction_date
        self.quantity = quantity
        self.total_price = total_price

# Sample Data
author1 = Author(1, "J.K. Rowling", "British author, best known for the Harry Potter series.")
book1 = Book(1, "Harry Potter and the Philosopher's Stone", author1, "Fantasy", 20.00, "1997-06-26")
author1.add_book(book1)

customer1 = Customer(1, "John Doe", "john.doe@example.com", "123-456-7890")

# Sample Transaction
transaction1 = Transaction(1, book1, customer1, "2023-07-15", 1, book1.price)

# Borrowing a book
customer1.borrow_book(book1)

# Display borrowed books
print(f"{customer1.name} borrowed: {[book.title for book in customer1.borrowed_books]}")

# Returning a book
customer1.return_book(book1)

# Display borrowed books after returning
print(f"{customer1.name} borrowed: {[book.title for book in customer1.borrowed_books]}")
