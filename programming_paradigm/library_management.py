class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)
        print(f"Added {book.title} to the library")

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Checked out {title}")
                    return True
                else:
                    print(f"{title} is already checked out")
                    return False
        print(f"{title} not found in the library")
        return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Returned {title}")
                    return True
                else:
                    print(f"{title} was not checked out")
                    return False
        print(f"{title} not found in the library")
        return False

    def list_available_books(self):
        print("Available books:")
        found = False
        for book in self._books:
            if book.is_available():
                print(f"- {book.title} by {book.author}")
                found = True
        if not found:
            print("No books available")
