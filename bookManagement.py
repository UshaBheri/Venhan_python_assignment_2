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

class Library:
    def __init__(self):
        self.books = {}

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



