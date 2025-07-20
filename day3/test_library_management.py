import unittest
from library_management import Library, Book, Member


class TestLibrarySystem(unittest.TestCase):

    def setUp(self):
        self.lib = Library()
        self.lib.add_book("The Hobbit", "J.R.R. Tolkien", 2)
        self.lib.add_book("1984", "George Orwell", 1)
        self.lib.add_member("Alice")

    def test_add_book(self):
        self.assertEqual(len(self.lib.books), 2)
        self.lib.add_book("Dune", "Frank Herbert", 3)
        self.assertEqual(len(self.lib.books), 3)

    def test_search_books(self):
        results = self.lib.search_books("hobbit")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "The Hobbit")

    def test_add_member(self):
        self.lib.add_member("Bob")
        self.assertEqual(len(self.lib.members), 2)
        self.assertEqual(self.lib.members[1].name, "Bob")

    def test_borrow_book_success(self):
        self.lib.borrow_book("Alice", "The Hobbit")
        member = self.lib.get_member_by_name("Alice")
        book = self.lib.get_book_by_title("The Hobbit")
        self.assertEqual(len(member.borrowed_books), 1)
        self.assertEqual(book.copies, 1)

    def test_borrow_book_not_found(self):
        self.lib.borrow_book("Alice", "Nonexistent Book")
        member = self.lib.get_member_by_name("Alice")
        self.assertEqual(len(member.borrowed_books), 0)

    def test_borrow_book_no_copies(self):
        self.lib.borrow_book("Alice", "1984")
        self.lib.add_member("Bob")
        self.lib.borrow_book("Bob", "1984")
        member2 = self.lib.get_member_by_name("Bob")
        self.assertEqual(len(member2.borrowed_books), 0)

    def test_borrow_book_limit(self):
        self.lib.add_book("Book1", "Author1", 1)
        self.lib.add_book("Book2", "Author2", 1)
        self.lib.add_book("Book3", "Author3", 1)

        self.lib.borrow_book("Alice", "The Hobbit")
        self.lib.borrow_book("Alice", "Book1")
        self.lib.borrow_book("Alice", "Book2")
        self.lib.borrow_book("Alice", "Book3")

        member = self.lib.get_member_by_name("Alice")
        self.assertEqual(len(member.borrowed_books), 3)

    def test_return_book_success(self):
        self.lib.borrow_book("Alice", "The Hobbit")
        self.lib.return_book("Alice", "The Hobbit")
        member = self.lib.get_member_by_name("Alice")
        book = self.lib.get_book_by_title("The Hobbit")
        self.assertEqual(len(member.borrowed_books), 0)
        self.assertEqual(book.copies, 2)

    def test_return_book_not_borrowed(self):
        self.lib.return_book("Alice", "1984")
        member = self.lib.get_member_by_name("Alice")
        self.assertEqual(len(member.borrowed_books), 0)


if __name__ == '__main__':
    unittest.main()
