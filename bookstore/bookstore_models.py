#!/usr/bin/env python3
from bookstore_management import Book

class Fiction(Book):
    def __init__(self, title, author, price, genre):
        super().__init__(title, author, price,)
        self.genre = genre
    
    def __str__(self):
        return f"{self.title} by {self.author} - ${self.price} - Genre: {self.genre}"
    
    def to_dict(self):
        return {
            "type": "Fiction",
            "title": self.title,
            "author": self.author,
            "price": self.price,
            "genre": self.genre
        }

class NonFiction(Book):
    def __init__(self, title, author, price, subject):
        super().__init__(title, author, price)
        self.subject = subject
    
    def __str__(self):
        return f"{self.title} by {self.author} - ${self.price} - Subject: {self.subject}"

    def to_dict(self):
        return {
            "type": "NonFiction",
            "title": self.title,
            "author": self.author,
            "price": self.price,
            "subject": self.subject
        }
    
class Textbook(Book):
    def __init__(self, title, author, price, course_name):
        super().__init__(title, author, price)
        self.course_name = course_name
    
    def __str__(self):
        return f"{self.title} by {self.author} - ${self.price} - Course: {self.course_name}"
    
    def to_dict(self):
        return {
            "type": "Textbook",
            "title": self.title,
            "author": self.author,
            "price": self.price,
            "course_name": self.course_name
        }
    
    #si se puedoo (:
    #posdata no llegue ni a leer el segundo trabajo y pushee el ultimo error a las 12:59
    