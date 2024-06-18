from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, ISBN, genre, quantity):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.genre = genre
        self.quantity = quantity

    def update_info(self, title=None, author=None, genre=None, quantity=None):
        if title:
            self.title = title
        if author:
            self.author = author
        if genre:
            self.genre = genre
        if quantity is not None:
            self.quantity = quantity

class Borrower:
    def __init__(self, name, contact_details, membership_id):
        self.name = name
        self.contact_details = contact_details
        self.membership_id = membership_id
        self.borrowed_books = {}  # ISBN -> due date

    def update_info(self, name=None, contact_details=None):
        if name:
            self.name = name
        if contact_details:
            self.contact_details = contact_details

class Library:
    def __init__(self):
        self.books = {}
        self.borrowers = {}

    def add_book(self, book):
        if book.ISBN in self.books:
            print(f"Book with ISBN {book.ISBN} already exists.")
        else:
            self.books[book.ISBN] = book
            print(f"Book '{book.title}' added to the library.")

    def update_book(self, ISBN, title=None, author=None, genre=None, quantity=None):
        if ISBN in self.books:
            self.books[ISBN].update_info(title, author, genre, quantity)
            print(f"Book with ISBN {ISBN} updated.")
        else:
            print(f"No book found with ISBN {ISBN}.")

    def remove_book(self, ISBN):
        if ISBN in self.books:
            del self.books[ISBN]
            print(f"Book with ISBN {ISBN} removed from the library.")
        else:
            print(f"No book found with ISBN {ISBN}.")

    def add_borrower(self, borrower):
        if borrower.membership_id in self.borrowers:
            print(f"Borrower with membership ID {borrower.membership_id} already exists.")
        else:
            self.borrowers[borrower.membership_id] = borrower
            print(f"Borrower '{borrower.name}' added to the library system.")

    def update_borrower(self, membership_id, name=None, contact_details=None):
        if membership_id in self.borrowers:
            self.borrowers[membership_id].update_info(name, contact_details)
            print(f"Borrower with membership ID {membership_id} updated.")
        else:
            print(f"No borrower found with membership ID {membership_id}.")

    def remove_borrower(self, membership_id):
        if membership_id in self.borrowers:
            del self.borrowers[membership_id]
            print(f"Borrower with membership ID {membership_id} removed from the library system.")
        else:
            print(f"No borrower found with membership ID {membership_id}.")

    # Borrowing and returning books
    def borrow_book(self, membership_id, ISBN, days_until_due):
        if membership_id in self.borrowers and ISBN in self.books:
            borrower = self.borrowers[membership_id]
            book = self.books[ISBN]
            if book.quantity > 0:
                book.quantity -= 1
                due_date = datetime.now() + timedelta(days=days_until_due)
                borrower.borrowed_books[ISBN] = due_date
                print(f"Book '{book.title}' borrowed by '{borrower.name}' and is due on {due_date.date()}.")
            else:
                print(f"Book '{book.title}' is not available for borrowing.")
        else:
            print("Invalid borrower ID or ISBN.")

    def return_book(self, membership_id, ISBN):
        if membership_id in self.borrowers and ISBN in self.borrowers[membership_id].borrowed_books:
            borrower = self.borrowers[membership_id]
            book = self.books[ISBN]
            due_date = borrower.borrowed_books[ISBN]
            del borrower.borrowed_books[ISBN]
            book.quantity += 1
            if datetime.now() > due_date:
                print(f"Book '{book.title}' returned late by '{borrower.name}'.")
            else:
                print(f"Book '{book.title}' returned on time by '{borrower.name}'.")
        else:
            print("Invalid borrower ID or ISBN.")

    def check_overdue_books(self):
        overdue_books = []
        for borrower in self.borrowers.values():
            for ISBN, due_date in borrower.borrowed_books.items():
                if datetime.now() > due_date:
                    overdue_books.append((borrower.name, self.books[ISBN].title, due_date.date()))
        return overdue_books

if __name__ == "__main__":
    library = Library()

    # Add books
    book1 = Book("1984", "R.K.Rowling", "1234567890", "Harry Potter", 5)
    library.add_book(book1)

    # Add borrowers
    borrower1 = Borrower("Usha", "usha@example.com", "B001")
    library.add_borrower(borrower1)

    # Borrow a book
    library.borrow_book("B001", "1234567890", 7)

    # Return a book on time
    library.return_book("B001", "1234567890")

    # Borrow the book again and return it late
    library.borrow_book("B001", "1234567890", 7)
    # Simulate the book being overdue by advancing the system time
    borrower1.borrowed_books["1234567890"] = datetime.now() - timedelta(days=1)
    library.return_book("B001", "1234567890")

    # Check overdue books
    overdue_books = library.check_overdue_books()
    print("Overdue Books:")
    for borrower_name, book_title, due_date in overdue_books:
        print(f"{borrower_name} has overdue book '{book_title}' which was due on {due_date}.")
