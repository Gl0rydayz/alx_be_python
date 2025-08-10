#!/usr/bin/env python3
"""
Simple test script to verify output format matches expected output.
"""

from library_system import Book, EBook, PrintBook, Library

def test_library_output():
    """Test the library output format."""
    # Create a library
    library = Library()
    
    # Create different types of books
    book1 = Book("Pride and Prejudice", "Jane Austen")
    ebook1 = EBook("Snow Crash", "Neal Stephenson", 500)
    printbook1 = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)
    
    # Add books to library
    library.add_book(book1)
    library.add_book(ebook1)
    library.add_book(printbook1)
    
    # Test the output format
    print("Books in the library:")
    for book in library.books:
        print(book.get_info())
    
    print(f"\nTotal books: {library.get_book_count()}")

if __name__ == "__main__":
    test_library_output() 