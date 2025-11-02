'Create a class Book with class variable total_books to count how many books are created'

class Book:
    total_book = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.total_book += 1

    def show(self):
        print(f"Title: {self.title}, Author: {self.author}")

book1 = Book("Python Basics", "John Doe")
book2 = Book("AI for Beginners", "CodeWithHarry")

book1.show()
book2.show()

print(f"Total Book Created: {Book.total_book}")