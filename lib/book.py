#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

# Create an instance of the Book class
my_book = Book("Caucasian Chalk Circle", 150)

# Access and print the attributes and methods
print(f"Title: {my_book.title}")
print(f"Page Count: {my_book.page_count}")

# Call the turn_page method
my_book.turn_page()
