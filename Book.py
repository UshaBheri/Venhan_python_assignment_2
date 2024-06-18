class Book:
    def __init__(self, title, author, ISBN, genre, quantity):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.genre = genre
        self.quantity = quantity

    def update_info(self, title=None, author=None, quantity=None):
        if title:
            self.title = title
        if author:
            self.author = author
        if quantity is not None:
            self.quantity = quantity

class Borrower:
    def __init__(self, name, contact_details, membership_id):
        self.name = name
        self.contact_details = contact_details
        self.membership_id = membership_id
        self.borrowed_books = {}

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
        self.books[book.ISBN] = book

    def update_book(self, ISBN, title=None, author=None, quantity=None):
        if ISBN in self.books:
            self.books[ISBN].update_info(title, author, quantity)

    def remove_book(self, ISBN):
        if ISBN in self.books:
            del self.books[ISBN]

    def add_borrower(self, borrower):
        self.borrowers[borrower.membership_id] = borrower

    def update_borrower(self, membership_id, name=None, contact_details=None):
        if membership_id in self.borrowers:
            self.borrowers[membership_id].update_info(name, contact_details)

    def remove_borrower(self, membership_id):
        if membership_id in self.borrowers:
            del self.borrowers[membership_id]

    def borrow_book(self, membership_id, ISBN, due_date):
        if membership_id in self.borrowers and ISBN in self.books:
            borrower = self.borrowers[membership_id]
            book = self.books[ISBN]
            if book.quantity > 0:
                book.quantity -= 1
                borrower.borrowed_books[ISBN] = due_date
            else:
                print(f"Book '{book.title}' is not available for borrowing.")

    def return_book(self, membership_id, ISBN):
        if membership_id in self.borrowers and ISBN in self.borrowers[membership_id].borrowed_books:
            borrower = self.borrowers[membership_id]
            book = self.books[ISBN]
            book.quantity += 1
            del borrower.borrowed_books[ISBN]

    def search_books(self, title=None, author=None, genre=None):
        results = []
        for book in self.books.values():
            if ((title and title.lower() in book.title.lower()) or
                (author and author.lower() in book.author.lower()) or
                (genre and genre.lower() in book.genre.lower())):
                results.append(book)
        return results

    def show_availability(self, ISBN):
        if ISBN in self.books:
            book = self.books[ISBN]
            return book.quantity
        return 0

if __name__ == "__main__":
    library = Library()

    # Add books
    book1 = Book("1984", "R.K.Rowling", "1234567890", "Harry Potter", 5)
    library.add_book(book1)

    # Update book
    library.update_book("1234567890", quantity=10)

    # Remove book
    library.remove_book("0987654321")

    # Try to update a non-existent book
    library.update_book("1111111111", title="Non-existent Book")

    # Try to remove a non-existent book
    library.remove_book("1111111111")

    # Add borrowers
    borrower1 = Borrower("Usha", "usha@example.com", "B001")
    
    library.add_borrower(borrower1)
    
    # Borrow a book
    library.borrow_book("B001", "1234567890", "2024-07-01")

    # Updating borrower's contact details
    library.update_borrower("B001", contact_details="usha_new@example.com")

    # Removing a borrower from the library system
    library.remove_borrower("B001")

    # Return a book
    library.return_book("B001", "1234567890")

    # Search for books
    results = library.search_books(title="1984")
    for book in results:
        print(book.title, book.author, book.ISBN, book.genre, book.quantity)

    # Check availability
    print(library.show_availability("1234567890"))
