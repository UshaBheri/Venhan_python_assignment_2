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

    # Book management methods (add_book, update_book, remove_book) 

    # Borrower management methods
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

# Creating the Library object
library = Library()

# Creating borrower objects
borrower1 = Borrower("Usha", "usha@example.com", "B001")

# Adding borrowers to the library system
library.add_borrower(borrower1)

# Updating borrower's contact details
library.update_borrower("B001", contact_details="usha_new@example.com")

# Removing a borrower from the library system
library.remove_borrower("B001")

