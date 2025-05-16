"""
Library Management System CLI
"""

from typing import List, Optional


class Book:
    def __init__(self, title: str, author: str, isbn: str, is_borrowed: bool = False):
        """Initialize a book with title, author, ISBN, and borrowed status."""
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = is_borrowed

    def __str__(self) -> str:
        status = 'Borrowed' if self.is_borrowed else 'Available'
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) — {status}"


class Library:
    def __init__(self):
        """Initialize an empty library."""
        self.books: List[Book] = []

    def add_book(self, book: Book) -> bool:
        """Add a new book if ISBN is unique."""
        if self.find_book_by_isbn(book.isbn):
            print(f"Error: A book with ISBN {book.isbn} already exists in the library.")
            return False
        self.books.append(book)
        print(f"Book added: {book}")
        return True

    def remove_book(self, isbn: str) -> bool:
        """Remove a book by ISBN."""
        book = self.find_book_by_isbn(isbn)
        if not book:
            print(f"No book with ISBN {isbn} found.")
            return False
        self.books.remove(book)
        print(f"Removed book: {book}")
        return True

    def borrow_book(self, isbn: str) -> bool:
        """Borrow a book if it's available."""
        book = self.find_book_by_isbn(isbn)
        if not book:
            print(f"No book with ISBN {isbn} found.")
            return False
        if book.is_borrowed:
            print(f"Sorry, '{book.title}' is already borrowed.")
            return False
        book.is_borrowed = True
        print(f"You have successfully borrowed '{book.title}'. Enjoy reading!")
        return True

    def return_book(self, isbn: str) -> bool:
        """Return a book if it was borrowed."""
        book = self.find_book_by_isbn(isbn)
        if not book:
            print(f"No book with ISBN {isbn} found.")
            return False
        if not book.is_borrowed:
            print(f"'{book.title}' was not borrowed.")
            return False
        book.is_borrowed = False
        print(f"Thank you for returning '{book.title}'.")
        return True

    def display_books(self) -> None:
        """Display all books with their status."""
        if not self.books:
            print("The library is currently empty.")
            return
        print("Library collection:")
        for idx, book in enumerate(self.books, start=1):
            print(f"{idx}. {book}")

    def find_book_by_isbn(self, isbn: str) -> Optional[Book]:
        """Find and return a book by its ISBN."""
        return next((b for b in self.books if b.isbn == isbn), None)


def get_valid_input(prompt: str, validator=None) -> str:
    """Prompt the user until they provide valid input."""
    while True:
        user_input = input(prompt).strip()
        if validator and not validator(user_input):
            print("Invalid input. Please try again.")
        else:
            return user_input


def main():
    library = Library()
    menu = """
--- Library Management ---
1. Add a new book
2. Remove a book
3. Borrow a book
4. Return a book
5. Show all books
6. Exit
"""
    while True:
        print(menu)
        choice = get_valid_input("Choose an option (1-6): ",
                                 lambda x: x in {'1','2','3','4','5','6'})
        if choice == '1':
            title = get_valid_input("Title: ", lambda x: len(x) > 0)
            author = get_valid_input("Author: ", lambda x: len(x) > 0)
            isbn = get_valid_input("ISBN (digits only): ",
                                    lambda x: x.isdigit())
            library.add_book(Book(title, author, isbn))
        elif choice == '2':
            isbn = get_valid_input("ISBN of the book to remove: ",
                                    lambda x: x.isdigit())
            library.remove_book(isbn)
        elif choice == '3':
            isbn = get_valid_input("ISBN of the book to borrow: ",
                                    lambda x: x.isdigit())
            library.borrow_book(isbn)
        elif choice == '4':
            isbn = get_valid_input("ISBN of the book to return: ",
                                    lambda x: x.isdigit())
            library.return_book(isbn)
        elif choice == '5':
            library.display_books()
        else:  # '6'
            print("Goodbye! Have a great day.")
            break


if __name__ == "__main__":
    main()
