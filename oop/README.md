# Python Magic Methods - Book Class Implementation

This project demonstrates the implementation of Python magic methods through a `Book` class that models books with title, author, and publication year.

## Files

- `book_class.py` - Contains the Book class with magic methods
- `main.py` - Test script to demonstrate the magic methods
- `README.md` - This documentation file

## Book Class Features

### Attributes
- `title` (str): The title of the book
- `author` (str): The author of the book  
- `year` (int): The publication year of the book

### Magic Methods Implemented

1. **`__init__(self, title, author, year)`** - Constructor
   - Initializes a new Book instance with the provided attributes
   - Uses type hints for better code clarity

2. **`__del__(self)`** - Destructor
   - Automatically called when the object is deleted
   - Prints "Deleting {title}" message

3. **`__str__(self)`** - String Representation
   - Returns user-friendly string format: "{title} by {author}, published in {year}"
   - Used by `print()` function and `str()` conversion

4. **`__repr__(self)`** - Official Representation
   - Returns a string that can recreate the object
   - Format: `Book('{title}', '{author}', {year})`
   - Used for debugging and development

## Usage

Run the test script to see all magic methods in action:

```bash
python main.py
```

### Expected Output
```
1984 by George Orwell, published in 1949
Book('1984', 'George Orwell', 1949)
Deleting 1984
```

## Learning Objectives

This implementation helps master:
- Python object-oriented programming concepts
- Magic methods (dunder methods) in Python
- Constructor and destructor patterns
- String representation methods
- Best practices for class design

## Code Quality Features

- Comprehensive docstrings for all methods
- Type hints for better code clarity
- Clean, readable code structure
- Follows PEP 8 style guidelines 