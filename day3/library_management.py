import uuid


class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.isbn = str(uuid.uuid4())[:13]
        self.copies = copies

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - Copies Available: {self.copies}"


class Member:
    def __init__(self, name):
        self.name = name
        self.member_id = str(uuid.uuid4())[:8]
        self.borrowed_books = []

    def __str__(self):
        return f"{self.name} (ID: {self.member_id}) - Borrowed: {[book.title for book in self.borrowed_books]}"


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author, copies):
        self.books.append(Book(title, author, copies))
        print("Book added successfully!")

    def search_books(self, keyword):
        results = [book for book in self.books if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()]
        return results

    def list_books(self):
        if not self.books:
            print("No books available.")
        for book in self.books:
            print(book)

    def add_member(self, name):
        member = Member(name)
        self.members.append(member)
        print(f"Member added successfully! Member ID: {member.member_id}")

    def list_members(self):
        if not self.members:
            print("No members registered.")
        for member in self.members:
            print(member)

    def get_member_by_name(self, name):
        for member in self.members:
            if member.name.lower() == name.lower():
                return member
        return None

    def get_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def borrow_book(self, member_name, book_title):
        member = self.get_member_by_name(member_name)
        book = self.get_book_by_title(book_title)

        if not member:
            print("Member not found.")
            return
        if not book:
            print("Book not found.")
            return
        if book.copies == 0:
            print("Book not available.")
            return
        if len(member.borrowed_books) >= 3:
            print("Borrow limit reached (3 books max).")
            return

        member.borrowed_books.append(book)
        book.copies -= 1
        print(f"{member.name} successfully borrowed '{book.title}'.")

    def return_book(self, member_name, book_title):
        member = self.get_member_by_name(member_name)
        book = self.get_book_by_title(book_title)

        if not member or not book:
            print("Invalid member or book.")
            return
        if book not in member.borrowed_books:
            print("This book was not borrowed by the member.")
            return

        member.borrowed_books.remove(book)
        book.copies += 1
        print(f"{member.name} returned '{book.title}'.")


def main():
    lib = Library()

    while True:
        print("\n=== Library Management Menu ===")
        print("1. Add Book")
        print("2. List Books")
        print("3. Search Book")
        print("4. Add Member")
        print("5. List Members")
        print("6. Borrow Book")
        print("7. Return Book")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Book Title: ")
            author = input("Author: ")
            try:
                copies = int(input("Number of Copies: "))
                lib.add_book(title, author, copies)
            except ValueError:
                print("Invalid number of copies.")
        elif choice == "2":
            lib.list_books()
        elif choice == "3":
            keyword = input("Enter title or author keyword: ")
            results = lib.search_books(keyword)
            if results:
                for book in results:
                    print(book)
            else:
                print("No books found.")
        elif choice == "4":
            name = input("Member Name: ")
            lib.add_member(name)
        elif choice == "5":
            lib.list_members()
        elif choice == "6":
            name = input("Enter Member Name: ")
            title = input("Enter Book Title: ")
            lib.borrow_book(name, title)
        elif choice == "7":
            name = input("Enter Member Name: ")
            title = input("Enter Book Title: ")
            lib.return_book(name, title)
        elif choice == "8":
            print("Exiting Library System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
