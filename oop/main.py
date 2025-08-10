from class_static_methods_demo import Calculator

def main():
    print("Calculator Class Methods and Static Methods Demo")
    print("=" * 50)
    
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")
    
    # Using another static method
    diff_result = Calculator.subtract(10, 5)
    print(f"The difference is: {diff_result}")
    
    print("\n" + "-" * 30)
    
    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")
    
    # Using another class method
    quotient_result = Calculator.divide(10, 2)
    print(f"The quotient is: {quotient_result}")
    
    print("\n" + "-" * 30)
    
    # Demonstrating class attribute access through class methods
    current_type = Calculator.get_calculation_type()
    print(f"Current calculation type: {current_type}")
    
    # Changing calculation type using class method
    Calculator.set_calculation_type("Advanced Mathematics")
    
    # Using class method again to see the change
    new_product = Calculator.multiply(8, 6)
    print(f"New product with updated type: {new_product}")
    
    print("\n" + "-" * 30)
    
    # Creating an instance to demonstrate instance methods
    calc = Calculator("My Calculator")
    print(calc.instance_method_example())
    
    # Using instance methods
    calc.add_to_history("10 + 5", 15)
    calc.add_to_history("10 * 5", 50)
    calc.add_to_history("10 / 2", 5)
    
    print("\nCalculation History:")
    for entry in calc.get_history():
        print(f"  {entry}")
    
    print("\n" + "-" * 30)
    
    # Demonstrating the difference between method types
    print("Method Type Comparison:")
    print(f"  Static method (add): {Calculator.add}")
    print(f"  Class method (multiply): {Calculator.multiply}")
    print(f"  Instance method: {calc.instance_method_example}")
    
    # Showing that static methods can be called on instances too
    print(f"\nStatic method called on instance: {calc.add(20, 30)}")
    
    # Showing that class methods can be called on instances too
    print(f"Class method called on instance: {calc.multiply(20, 30)}")

if __name__ == "__main__":
    main() 