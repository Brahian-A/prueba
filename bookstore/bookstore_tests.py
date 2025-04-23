import unittest
from bookstore_management import Book, create_book, save_book_data, load_book_data, main
from bookstore_models import Fiction, NonFiction, Textbook
import os
import io
import sys


class TestBook(unittest.TestCase):

    def test_book_init(self):
        book = Book("Book Title", "Author Name", 29.99)
        self.assertEqual(book.title, "Book Title")
        self.assertEqual(book.author, "Author Name")
        self.assertEqual(book.price, 29.99)

    def test_str(self):
        book = Book("Book Title", "Author Name", 29.99)
        book_str = str(book)
        self.assertIn(book.title, book_str)
        self.assertIn(book.author, book_str)
        self.assertIn(str(book.price), book_str)

    def test_serialize_deserialize(self):
        book = Book("Book Title", "Author Name", 29.99)
        save_book_data(book)
        self.assertTrue(os.path.exists(f"{book.title}_{book.author}.json"))

        deserialized_book = load_book_data(book.title, book.author)
        self.assertIsInstance(deserialized_book, Book)
        self.assertEqual(book.title, deserialized_book.title)
        self.assertEqual(book.author, deserialized_book.author)
        self.assertEqual(book.price, deserialized_book.price)
        os.remove(f"{book.title}_{book.author}.json")


class TestBookSubclasses(unittest.TestCase):

    def test_fiction_init(self):
        fiction_book = Fiction("Fiction Book Title",
                               "Fiction Author", 24.99, "Mystery")
        self.assertEqual(fiction_book.title, "Fiction Book Title")
        self.assertEqual(fiction_book.author, "Fiction Author")
        self.assertEqual(fiction_book.price, 24.99)
        self.assertEqual(fiction_book.genre, "Mystery")

    def test_non_fiction_init(self):
        non_fiction_book = NonFiction(
            "Non-Fiction Book", "Non-Fiction Author", 19.99, "Science")
        self.assertEqual(non_fiction_book.title, "Non-Fiction Book")
        self.assertEqual(non_fiction_book.author, "Non-Fiction Author")
        self.assertEqual(non_fiction_book.price, 19.99)
        self.assertEqual(non_fiction_book.subject, "Science")

    def test_textbook_init(self):
        textbook = Textbook(
            "Textbook Title", "Textbook Author", 34.99, "Computer Science")
        self.assertEqual(textbook.title, "Textbook Title")
        self.assertEqual(textbook.author, "Textbook Author")
        self.assertEqual(textbook.price, 34.99)
        self.assertEqual(textbook.course_name, "Computer Science")

    def test_serialize_deserialize_subclass_fiction(self):
        book = Fiction("Book Title 2", "Author Name", 29.99, "Mystery")
        save_book_data(book)
        self.assertTrue(os.path.exists(f"{book.title}_{book.author}.json"))

        deserialized_book: Fiction = load_book_data(book.title, book.author)
        self.assertIsInstance(deserialized_book, Book)
        self.assertIsInstance(deserialized_book, Fiction)
        self.assertEqual(book.title, deserialized_book.title)
        self.assertEqual(book.author, deserialized_book.author)
        self.assertEqual(book.price, deserialized_book.price)
        self.assertEqual(book.genre, deserialized_book.genre)
        os.remove(f"{book.title}_{book.author}.json")

    def test_serialize_deserialize_subclass_nonfiction(self):
        book = NonFiction("Book Title 2", "Author Name", 29.99, "geography")
        save_book_data(book)
        self.assertTrue(os.path.exists(f"{book.title}_{book.author}.json"))

        deserialized_book: NonFiction = load_book_data(book.title, book.author)
        self.assertIsInstance(deserialized_book, Book)
        self.assertIsInstance(deserialized_book, NonFiction)
        self.assertEqual(book.title, deserialized_book.title)
        self.assertEqual(book.author, deserialized_book.author)
        self.assertEqual(book.price, deserialized_book.price)
        self.assertEqual(book.subject, deserialized_book.subject)
        os.remove(f"{book.title}_{book.author}.json")

    def test_serialize_deserialize_subclass_textbook(self):
        book = Textbook("Book Title 2", "Author Name",
                        29.99, "Computer Science")
        save_book_data(book)
        self.assertTrue(os.path.exists(f"{book.title}_{book.author}.json"))

        deserialized_book: Textbook = load_book_data(book.title, book.author)
        self.assertIsInstance(deserialized_book, Book)
        self.assertIsInstance(deserialized_book, Textbook)
        self.assertEqual(book.title, deserialized_book.title)
        self.assertEqual(book.author, deserialized_book.author)
        self.assertEqual(book.price, deserialized_book.price)
        self.assertEqual(book.course_name, deserialized_book.course_name)
        os.remove(f"{book.title}_{book.author}.json")

    def test_str_fiction(self):
        book = Fiction("Book Title", "Author Name", 29.99, "Epic")
        book_str = str(book)
        self.assertIn(book.title, book_str)
        self.assertIn(book.author, book_str)
        self.assertIn(str(book.price), book_str)
        self.assertIn(book.genre, book_str)

    def test_str_nonfiction(self):
        book = NonFiction("Book Title", "Author Name", 29.99, "geography")
        book_str = str(book)
        self.assertIn(book.title, book_str)
        self.assertIn(book.author, book_str)
        self.assertIn(str(book.price), book_str)
        self.assertIn(book.subject, book_str)

    def test_str_texbook(self):
        book = Textbook("Book Title", "Author Name", 29.99, "Computer Science")
        book_str = str(book)
        self.assertIn(book.title, book_str)
        self.assertIn(book.author, book_str)
        self.assertIn(str(book.price), book_str)
        self.assertIn(book.course_name, book_str)


class TestMainProgram(unittest.TestCase):

    def test_create_book(self):
        book_type = "Fiction"
        title = "Sample Fiction Book"
        author = "John Doe"
        price = 29.99
        unique_attribute = "Mystery"

        book = create_book(book_type, title, author, price, unique_attribute)
        self.assertIsInstance(book, Fiction)
        self.assertEqual(book.title, title)
        self.assertEqual(book.author, author)
        self.assertEqual(book.price, price)
        self.assertEqual(book.genre, unique_attribute)

    def test_save_load_book_data(self):
        book = Fiction("Fiction Book", "Fiction Author", 24.99, "Thriller")
        save_book_data(book)
        self.assertTrue(os.path.exists(f"{book.title}_{book.author}.json"))
        loaded_book = load_book_data("Fiction Book", "Fiction Author")
        self.assertIsInstance(loaded_book, Fiction)
        self.assertEqual(loaded_book.title, book.title)
        self.assertEqual(loaded_book.author, book.author)
        self.assertEqual(loaded_book.price, book.price)
        self.assertEqual(loaded_book.genre, book.genre)

        os.remove(f"{book.title}_{book.author}.json")

    def test_main_program_create(self):
        """ main program call create book function test """
        original_stdout = sys.stdout
        output_buffer = io.StringIO()
        sys.stdout = output_buffer

        main(["create", "Fiction", "Fiction Book",
             "Fiction Author", "24.99", "Thriller"])

        sys.stdout = original_stdout
        captured_output = output_buffer.getvalue()
        self.assertIn("Fiction Book", captured_output)
        self.assertIn("Fiction Author", captured_output)
        self.assertIn("24.99", captured_output)
        self.assertIn("Thriller", captured_output)
        self.assertTrue(os.path.exists("Fiction Book_Fiction Author.json"))
        loaded_book = load_book_data("Fiction Book", "Fiction Author")
        self.assertIsInstance(loaded_book, Fiction)
        self.assertEqual(loaded_book.title, "Fiction Book")
        self.assertEqual(loaded_book.author, "Fiction Author")
        self.assertEqual(loaded_book.price, 24.99)
        self.assertEqual(loaded_book.genre, "Thriller")
        os.remove("Fiction Book_Fiction Author.json")

    def test_main_program_load(self):
        """ main program call load book function test """
        book = create_book("Fiction", "Fiction Book",
                           "Fiction Author", 24.99, "Thriller")
        save_book_data(book)

        original_stdout = sys.stdout
        output_buffer = io.StringIO()
        sys.stdout = output_buffer

        main(["load", book.title, book.author])

        sys.stdout = original_stdout
        captured_output = output_buffer.getvalue()
        self.assertIn("Fiction Book", captured_output)
        self.assertIn("Fiction Author", captured_output)
        self.assertIn("24.99", captured_output)
        self.assertIn("Thriller", captured_output)
        self.assertTrue(os.path.exists(f"{book.title}_{book.author}.json"))
        loaded_book = load_book_data("Fiction Book", "Fiction Author")
        self.assertIsInstance(loaded_book, Fiction)
        self.assertEqual(loaded_book.title, "Fiction Book")
        self.assertEqual(loaded_book.author, "Fiction Author")
        self.assertEqual(loaded_book.price, 24.99)
        self.assertEqual(loaded_book.genre, "Thriller")
        os.remove("Fiction Book_Fiction Author.json")


if __name__ == "__main__":
    unittest.main()