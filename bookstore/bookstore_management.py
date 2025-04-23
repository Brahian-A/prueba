#!/usr/bin/env python3
from abc import ABC, abstractmethod
import json
import os


class Book(ABC):
    def __init__(self, title, author, price= 0):
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a positiver number")
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author} - ${self.price}"

    
    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "author": self.author,
            "price": self.price,
            'type': Book.__class__.__name__,
        }
    
def save_book_data(book):
    filename = f"{book.title}_{book.author}.json"

    with open(filename, "w") as file:
        json.dump(book.to_dict(), file, indent=4)

def load_book_data(title, author):
    from bookstore_models import Fiction, NonFiction, Textbook
    filename = f"{title}_{author}.json"
    with open(filename, "r") as f:
        data = json.load(f)
    if data['type'] == 'Fiction':
        return Fiction(data['title'], data['author'], data['price'], data['genre'])
    elif data['type'] == 'NonFiction':
        return NonFiction(data['title'], data['author'], data['price'], data['subject'])
    elif data['type'] == 'Textbook':
        return Textbook(data['title'], data['author'], data['price'], data['course_name'])
    else:
        return Book(data["title"], data["author"], data["price"])

def create_book(book_type: str, title: str, author: str, price: float, unique_attribute: str | None = None) -> Book:
    from bookstore_models import Fiction, NonFiction, Textbook
    if book_type == "Fiction":
        return Fiction(title, author, price, unique_attribute)
    elif book_type == "NonFiction":
        return NonFiction(title, author, price, unique_attribute)
    elif book_type == "Textbook":
        return Textbook(title, author, price, unique_attribute)
    else:
        raise ValueError(f"Unknown book type: {book_type}")

def main(argv: list) -> None:
    command = argv[0]
    if command == "create":
        book_type = argv[1]
        title = argv[2]
        author = argv[3]
        price = float(argv[4])
        unique_attribute = argv[5] if len(argv) > 5 else None
        book = create_book(book_type, title, author, price, unique_attribute)
        print(book)
        save_book_data(book)
    elif command == "load":
        title = argv[1]
        author = argv[2]
        book = load_book_data(title, author)
        if book:
            print(book)
        else:
            print("Book not found.")
