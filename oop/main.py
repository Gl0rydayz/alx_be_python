#!/usr/bin/env python3
"""
Main test script for OOP concepts demonstration.
Tests magic methods, inheritance, composition, and class/static methods.
"""

from book_class import Book
from library_system import Book as LibraryBook, EBook, PrintBook, Library
from class_static_methods_demo import Calculator

def test_magic_methods():
    """Test the Book class magic methods."""
    print("=" * 50)
    print("TESTING MAGIC METHODS")
    print("=" * 50)
    
    # Create a book instance
    my_book = Book("1984", "George Orwell", 1949)
    
    # Test __str__ method
    print(f"String representation: {my_book}")
    
    # Test __repr__ method
    print(f"Official representation: {repr(my_book)}")
    
    # Test __del__ method
    del my_book
    print()

def test_inheritance_and_composition():
    """Test inheritance and composition with the library system."""
    print("=" * 50)
    print("TESTING INHERITANCE AND COMPOSITION")
    print("=" * 50)
    
    # Create a library
    library = Library()
    
    # Create different types of books
    book1 = LibraryBook("The Great Gatsby", "F. Scott Fitzgerald")
    ebook1 = EBook("Python Programming", "John Smith", 2048)
    printbook1 = PrintBook("Data Structures", "Jane Doe", 450)
    
    # Test __str__ methods
    print(f"Book: {book1}")
    print(f"EBook: {ebook1}")
    print(f"PrintBook: {printbook1}")
    print()
    
    # Add books to library (composition)
    library.add_book(book1)
    library.add_book(ebook1)
    library.add_book(printbook1)
    
    # List all books
    library.list_books()
    print(f"Total books in library: {library.get_book_count()}")
    print()

def test_class_and_static_methods():
    """Test class methods and static methods."""
    print("=" * 50)
    print("TESTING CLASS AND STATIC METHODS")
    print("=" * 50)
    
    # Test static methods
    sum_result = Calculator.add(10, 5)
    print(f"Static method add result: {sum_result}")
    
    diff_result = Calculator.subtract(10, 5)
    print(f"Static method subtract result: {diff_result}")
    
    # Test class methods
    product_result = Calculator.multiply(10, 5)
    print(f"Class method multiply result: {product_result}")
    
    quotient_result = Calculator.divide(10, 2)
    print(f"Class method divide result: {quotient_result}")
    
    # Test class attribute access
    current_type = Calculator.get_calculation_type()
    print(f"Current calculation type: {current_type}")
    
    # Change calculation type
    Calculator.set_calculation_type("Advanced Mathematics")
    
    # Test instance methods
    calc = Calculator("My Calculator")
    print(f"Instance method: {calc.instance_method_example()}")
    
    # Add to history
    calc.add_to_history("10 + 5", 15)
    calc.add_to_history("10 * 5", 50)
    
    print("Calculation History:")
    for entry in calc.get_history():
        print(f"  {entry}")
    print()

def main():
    """Main function to run all tests."""
    print("OOP CONCEPTS DEMONSTRATION")
    print("Testing all implementations...")
    print()
    
    try:
        test_magic_methods()
        test_inheritance_and_composition()
        test_class_and_static_methods()
        
        print("=" * 50)
        print("ALL TESTS COMPLETED SUCCESSFULLY!")
        print("=" * 50)
        
    except Exception as e:
        print(f"Error during testing: {e}")
        print("Please check the implementation.")

if __name__ == "__main__":
    main() 