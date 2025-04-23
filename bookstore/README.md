# Bookstore Management System

## Introduction

In this exercise, you will create a simple bookstore management system using Python. You will design a set of classes representing different types of books and their characteristics. The exercise will cover object-oriented programming, inheritance, basic Python data structures and functions, and JSON data serialization.

### Part 1: Creating Book classes

In the `module` named `bookstore_management.py`:

Create an **abstract class** named `Book` with the following attributes:

- `title`
- `author`
- `price`

Define an `__init__` method for the class, taking title, author and price as parameters and initializing the corresponding attributes.

Define a method `__str__` that returns the book's information in a user-friendly format.

```python
>>> from bookstore_management import Book
>>> book = Book("The Odyssey", "Homer", 19.99)
>>> print(book)
The Odyssey by Homer - $19.99
```

In the `module` named `bookstore_models.py` create three subclasses: `Fiction`, `NonFiction`, and `Textbook`. Each subclass should inherit from the `Book` class and add a unique attribute:

- Fiction: genre
- NonFiction: subject
- Textbook: course_name

Define an `__init__` method for each subclass that takes the unique attribute as an additional parameter, calls the parent class's `__init__` method, and initializes the unique attribute.

Override the `__str__` method in each subclass to return the unique attribute along with the base attributes.

```python
>>> from bookstore_models import Fiction
>>> fiction_book = Fiction("The Odyssey", "Homer", 19.99, "Epic")
>>> print(fiction_book)
The Odyssey by Homer - $19.99 - Genre: Epic
The Odyssey by Homer - $19.99 - Genre: Epic
```

### Part 2: Serialization and storage

> `module: bookstore_management.py`

Add a **method** `to_dict(self) -> dict` to the `Book` class that converts the book object to a dictionary.

Create a **function** `save_book_data(book_obj: Book) -> None` that takes a Book object as input, serializes it, and writes the JSON string to a file named `<book_obj.title>_<book_obj.author>.json`.

```bash
$ python3
>>> from bookstore_management import Book, save_book_data
>>> book = Book("The Odyssey", "Homer", 19.99)
>>> save_book_data(book)
>>>
$ ls -1
README.md
'The Odyssey_Homer.json'
bookstore_management.py
bookstore_models.py
```

Create a **function** `load_book_data(title: str, author: str) -> Book:` that reads the JSON string from the file `<title>_<author>.json` and returns a Book object (or one of its subclasses).

```python3
>>> from bookstore_management import load_book_data
>>> book = load_book_data("The Odyssey", "Homer")
>>> print(book)
The Odyssey by Homer - $19.99
```

### Part 3: Main program

1. Create a **function** `create_book(book_type: str, title: str, author: str, price: float, unique_attribute: str | None = None) -> Book:` that does the following:

- Takes the `book_type` (Fiction, NonFiction, Textbook or Book) and book attributes as parameters.
- Creates an object of the appropriate class with the provided attributes.
- Returns the created object.

```python
>>> from bookstore_management import create_book
>>> fiction_book = create_book("Fiction", "The Odyssey", "Homer", 19.99, "Epic")
>>> print(fiction_book)
The Odyssey by Homer - $19.99 - Genre: Epic
>>> type(fiction_book)
<class 'bookstore_models.Fiction'>
>>> book = create_book("Book", "Pirates of the Caribbean", "Jack Sparrow", 9.99)
>>> print(book)
Pirates of the Caribbean by Jack Sparrow - $9.99
```

1. Create a **function** `main(argv: list) -> None` that does the following:

argv is a list of strings containing the command line arguments. The first argument is the command to execute (create or load). The remaining arguments are the book attributes.

- If the command is `create`:
  - The first argument is the book type (Fiction, NonFiction, Textbook or Book).
  - The remaining arguments are the book attributes.
  - Call `create_book()` with the provided arguments and store the returned object.
  - **Print the book's information.**
  - Call `save_book_data()` with the returned object.

- If the command is `load`:
  - The first argument is the book title.
  - The second argument is the book author.
  - Call `load_book_data()` with the provided arguments and store the returned object.
  - **Print the book's information.**

```bash
$ python3 bookstore_management.py create Fiction "The Odyssey" Homer 19.99 Epic
The Odyssey by Homer - $19.99 - Genre: Epic
$ ls -1
README.md
'The Odyssey_Homer.json'
bookstore_management.py
bookstore_models.py
$ python3 bookstore_management.py load "The Odyssey" Homer
The Odyssey by Homer - $19.99
```

You can use this snippet of code at the end of the file to call the main function with the command line arguments.

```python
if __name__ == "__main__":
    from sys import argv

    if len(argv) < 2:
        print("Usage: ./bookstore_management.py <create/load> <args>")
        exit(1)

    # Remove the program name from argv
    main(argv[1:])
```

### Take your time and think about the problem before you start coding. Good luck! :)
