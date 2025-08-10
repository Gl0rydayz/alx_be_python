# Python Object-Oriented Programming (OOP) Concepts

This project demonstrates various Python OOP concepts through practical implementations.

## Files Overview

- **`book_class.py`** - Magic methods demonstration
- **`library_system.py`** - Inheritance and composition demonstration  
- **`class_static_methods_demo.py`** - Class and static methods demonstration
- **`polymorphism_demo.py`** - Polymorphism demonstration
- **`main.py`** - Comprehensive test script for all implementations

## 1. Magic Methods (`book_class.py`)

### Book Class Features
- **Attributes**: `title`, `author`, `year`
- **Magic Methods**:
  - `__init__(self, title, author, year)` - Constructor
  - `__del__(self)` - Destructor (prints deletion message)
  - `__str__(self)` - String representation
  - `__repr__(self)` - Official representation

### Expected Output
```
1984 by George Orwell, published in 1949
Book('1984', 'George Orwell', 1949)
Deleting 1984
```

## 2. Inheritance and Composition (`library_system.py`)

### Class Hierarchy
- **Base Class**: `Book`
  - Attributes: `title`, `author`
  - Methods: `get_info()`, `__str__()`

- **Derived Class**: `EBook` (inherits from `Book`)
  - Additional attribute: `file_size`
  - Overrides `get_info()` and `__str__()`

- **Derived Class**: `PrintBook` (inherits from `Book`)
  - Additional attribute: `page_count`
  - Overrides `get_info()` and `__str__()`

- **Composition Class**: `Library`
  - Contains a list of `Book` instances
  - Methods: `add_book()`, `list_books()`, `get_book_count()`

### Key Concepts Demonstrated
- **Inheritance**: `EBook` and `PrintBook` inherit from `Book`
- **Method Overriding**: Each derived class overrides `get_info()` and `__str__()`
- **Composition**: `Library` contains `Book` objects
- **Polymorphism**: Different book types can be treated uniformly

## 3. Class and Static Methods (`class_static_methods_demo.py`)

### Calculator Class Features
- **Class Attribute**: `calculation_type = "Arithmetic Operations"`

- **Static Methods**:
  - `add(a, b)` - Addition operation
  - `subtract(a, b)` - Subtraction operation

- **Class Methods**:
  - `multiply(cls, a, b)` - Multiplication with class attribute access
  - `divide(cls, a, b)` - Division with class attribute access
  - `get_calculation_type(cls)` - Get current calculation type
  - `set_calculation_type(cls, new_type)` - Change calculation type

- **Instance Methods**:
  - `instance_method_example()` - Access to both instance and class attributes
  - `add_to_history()` - Instance-specific operations
  - `get_history()` - Instance-specific data retrieval

### Method Type Differences
- **Static Methods**: No access to class or instance attributes
- **Class Methods**: Access to class attributes via `cls` parameter
- **Instance Methods**: Access to both instance and class attributes

## 4. Polymorphism (`polymorphism_demo.py`)

### Shape Class Hierarchy
- **Base Class**: `Shape`
  - Abstract `area()` method raising `NotImplementedError`

- **Derived Classes**:
  - `Rectangle`: `area() = length × width`
  - `Circle`: `area() = π × radius²`
  - `Triangle`: `area() = 0.5 × base × height`

### Polymorphic Behavior
- All shapes can be treated uniformly through the `Shape` interface
- `area()` method is called polymorphically on different shape types
- Demonstrates method overriding and runtime dispatch

## Running the Tests

Execute the comprehensive test script:

```bash
cd oop
python main.py
```

This will test all implementations and demonstrate:
1. Magic methods functionality
2. Inheritance and composition relationships
3. Class and static method behavior
4. Polymorphic method calls

## Learning Objectives

This project helps master:
- Python magic methods (dunder methods)
- Object-oriented programming principles
- Inheritance and method overriding
- Composition and object relationships
- Polymorphism and abstract base classes
- Class methods vs static methods vs instance methods
- Best practices for Python class design

## Code Quality Features

- Comprehensive docstrings for all methods
- Type hints for better code clarity
- Error handling and validation
- Clean, readable code structure
- Follows PEP 8 style guidelines
- Practical examples with real-world scenarios 