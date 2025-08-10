# Python Class Methods and Static Methods - Calculator Demo

This project demonstrates the differences between class methods and static methods in Python through a practical Calculator class implementation. It showcases when and how to use `@classmethod` and `@staticmethod` decorators.

## Files

- `class_static_methods_demo.py` - Contains the Calculator class with class and static methods
- `main.py` - Test script demonstrating the different method types
- `README.md` - This documentation file

## Class Structure

### Calculator Class Methods

```
Calculator
├── Class Attributes
│   └── calculation_type = "Arithmetic Operations"
├── Static Methods (@staticmethod)
│   ├── add(a, b)
│   └── subtract(a, b)
├── Class Methods (@classmethod)
│   ├── multiply(cls, a, b)
│   ├── divide(cls, a, b)
│   ├── get_calculation_type(cls)
│   └── set_calculation_type(cls, new_type)
└── Instance Methods
    ├── __init__(self, name)
    ├── instance_method_example(self)
    ├── add_to_history(self, operation, result)
    └── get_history(self)
```

## Method Types Explained

### 1. Static Methods (@staticmethod)
**Purpose**: Independent functions that belong to the class namespace.

**Characteristics**:
- No access to class or instance attributes
- No `self` or `cls` parameter
- Can be called on the class or instances
- Independent of class state
- Useful for utility functions

**Examples in Calculator**:
- `add(a, b)`: Simple addition without class context
- `subtract(a, b)`: Simple subtraction without class context

**Usage**:
```python
# Called on class
result = Calculator.add(10, 5)

# Called on instance
calc = Calculator()
result = calc.add(10, 5)
```

### 2. Class Methods (@classmethod)
**Purpose**: Methods that have access to class attributes and can modify class state.

**Characteristics**:
- First parameter is `cls` (class reference)
- Access to class attributes and methods
- Can modify class state
- Can be called on class or instances
- Useful for factory methods and class-level operations

**Examples in Calculator**:
- `multiply(cls, a, b)`: Accesses `cls.calculation_type`
- `divide(cls, a, b)`: Accesses `cls.calculation_type`
- `get_calculation_type(cls)`: Returns class attribute
- `set_calculation_type(cls, new_type)`: Modifies class attribute

**Usage**:
```python
# Called on class
result = Calculator.multiply(10, 5)

# Called on instance
calc = Calculator()
result = calc.multiply(10, 5)
```

### 3. Instance Methods
**Purpose**: Methods that operate on instance-specific data.

**Characteristics**:
- First parameter is `self` (instance reference)
- Access to both instance and class attributes
- Can modify instance state
- Must be called on instances

**Examples in Calculator**:
- `instance_method_example(self)`: Accesses instance and class attributes
- `add_to_history(self, operation, result)`: Modifies instance state
- `get_history(self)`: Returns instance-specific data

## Key Differences

| Aspect | Static Method | Class Method | Instance Method |
|--------|---------------|--------------|-----------------|
| **First Parameter** | None | `cls` | `self` |
| **Class Access** | No | Yes | Yes |
| **Instance Access** | No | No | Yes |
| **State Modification** | No | Class state only | Instance state |
| **Calling** | Class/Instance | Class/Instance | Instance only |
| **Use Case** | Utility functions | Class operations | Instance operations |

## Practical Applications

### Static Methods
- **Utility Functions**: Mathematical operations, data validation
- **Helper Functions**: String formatting, data conversion
- **Pure Functions**: Functions with no side effects

### Class Methods
- **Factory Methods**: Creating instances with different configurations
- **Class Configuration**: Modifying class-level settings
- **Alternative Constructors**: Creating objects in different ways
- **Class State Management**: Accessing and modifying class attributes

### Instance Methods
- **Object Behavior**: Methods that operate on instance data
- **State Management**: Modifying instance attributes
- **Instance-Specific Logic**: Operations unique to each object

## Usage Examples

### Basic Operations
```python
# Static methods for simple calculations
sum_result = Calculator.add(10, 5)
diff_result = Calculator.subtract(10, 5)

# Class methods with class context
product_result = Calculator.multiply(10, 5)
quotient_result = Calculator.divide(10, 2)
```

### Class State Management
```python
# Getting current calculation type
current_type = Calculator.get_calculation_type()

# Changing calculation type
Calculator.set_calculation_type("Advanced Mathematics")

# Using updated type
new_result = Calculator.multiply(8, 6)
```

### Instance Operations
```python
# Creating calculator instance
calc = Calculator("My Calculator")

# Using instance methods
calc.add_to_history("10 + 5", 15)
history = calc.get_history()
```

## Expected Output

```
Calculator Class Methods and Static Methods Demo
==================================================
The sum is: 15
The difference is: 5

------------------------------
Calculation type: Arithmetic Operations
The product is: 50
Calculation type: Arithmetic Operations
The quotient is: 5.0

------------------------------
Current calculation type: Arithmetic Operations
Calculation type changed to: Advanced Mathematics
Calculation type: Advanced Mathematics
New product with updated type: 48

------------------------------
Calculator 'My Calculator' - Type: Advanced Mathematics

Calculation History:
  10 + 5: 15
  10 * 5: 50
  10 / 2: 5

------------------------------
Method Type Comparison:
  Static method (add): <function Calculator.add at 0x...>
  Class method (multiply): <bound method Calculator.multiply of <class '__main__.Calculator'>>
  Instance method: <bound method Calculator.instance_method_example of <__main__.Calculator object at 0x...>>

Static method called on instance: 50
Calculation type: Advanced Mathematics
Class method called on instance: 600
```

## Learning Objectives

This implementation helps master:
- **Static Methods**: Understanding utility functions in class context
- **Class Methods**: Managing class-level state and operations
- **Method Decorators**: Proper use of `@staticmethod` and `@classmethod`
- **Method Types**: Differences between static, class, and instance methods
- **Class State**: Managing and modifying class attributes
- **Design Patterns**: When to use each method type

## Code Quality Features

- Comprehensive docstrings for all methods
- Type hints for better code clarity and IDE support
- Clear separation between different method types
- Practical examples of each method type
- Error handling (e.g., division by zero)
- Follows PEP 8 style guidelines
- Demonstrates best practices in method design

## Advanced Concepts

- **Method Binding**: Understanding how methods are bound to classes/instances
- **Class State Persistence**: How class attributes persist across instances
- **Method Resolution Order**: How Python resolves method calls
- **Decorator Patterns**: Using decorators for method modification
- **Factory Pattern**: Using class methods as alternative constructors

## Best Practices

1. **Use Static Methods For**:
   - Pure utility functions
   - Functions that don't need class context
   - Mathematical operations

2. **Use Class Methods For**:
   - Factory methods
   - Class configuration
   - Class state management

3. **Use Instance Methods For**:
   - Object-specific behavior
   - Instance state modification
   - Instance-specific operations

This demonstration provides a solid foundation for understanding when and how to use different method types in Python, helping you make informed decisions about method design in your own classes. 