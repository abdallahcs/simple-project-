from library import Library
from book import Book
from patron import Patron

def main():
    library = Library()

    while True:
        action = input("Choose an action: [add_book, add_patron, borrow, return, display, exit]: ").strip().lower()

        if action == 'add_book':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            book = Book(title, author, isbn)
            library.add_book(book)
            print("Book added.")

        elif action == 'add_patron':
            name = input("Enter patron name: ")
            membership_id = input("Enter membership ID: ")
            patron = Patron(name, membership_id)
            library.add_patron(patron)
            print("Patron added.")

        elif action == 'borrow':
            isbn = input("Enter ISBN of the book to borrow: ")
            patron_name = input("Enter patron name: ")
            patron = next((p for p in library.patrons if p.name == patron_name), None)
            if patron:
                library.borrow_book(isbn, patron)
            else:
                print("Patron not found.")

        elif action == 'return':
            isbn = input("Enter ISBN of the book to return: ")
            library.return_book(isbn)

        elif action == 'display':
            for book in library.books:
                print(book)

        elif action == 'exit':
            break

        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()