class Calculator:
    """
    Calculator class demonstrating class methods and static methods.
    
    This class showcases the differences between @classmethod and @staticmethod
    decorators and their practical applications.
    """
    
    # Class attribute that can be accessed by class methods
    calculation_type = "Arithmetic Operations"
    
    def __init__(self, name: str = "Default Calculator"):
        """
        Initialize a Calculator instance.
        
        Args:
            name (str): The name of the calculator instance
        """
        self.name = name
        self.history = []
    
    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        
        Static methods don't have access to class or instance attributes.
        They are independent functions that belong to the class namespace.
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Sum of the two numbers
        """
        return a + b
    
    @staticmethod
    def subtract(a, b):
        """
        Static method to subtract two numbers.
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Difference of the two numbers
        """
        return a - b
    
    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers.
        
        Class methods have access to class attributes and methods through
        the cls parameter, but not instance attributes.
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Product of the two numbers
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
    
    @classmethod
    def divide(cls, a, b):
        """
        Class method to divide two numbers.
        
        Args:
            a (float): First number (dividend)
            b (float): Second number (divisor)
            
        Returns:
            float: Quotient of the two numbers
            
        Raises:
            ZeroDivisionError: If b is zero
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        
        print(f"Calculation type: {cls.calculation_type}")
        return a / b
    
    @classmethod
    def get_calculation_type(cls) -> str:
        """
        Class method to get the calculation type.
        
        Demonstrates accessing class attributes from a class method.
        
        Returns:
            str: The current calculation type
        """
        return cls.calculation_type
    
    @classmethod
    def set_calculation_type(cls, new_type: str) -> None:
        """
        Class method to change the calculation type.
        
        Demonstrates modifying class attributes from a class method.
        
        Args:
            new_type (str): New calculation type to set
        """
        cls.calculation_type = new_type
        print(f"Calculation type changed to: {new_type}")
    
    def instance_method_example(self) -> str:
        """
        Instance method example for comparison.
        
        This method has access to both instance and class attributes.
        
        Returns:
            str: Information about the calculator instance
        """
        return f"Calculator '{self.name}' - Type: {self.calculation_type}"
    
    def add_to_history(self, operation: str, result: float) -> None:
        """
        Instance method to add calculations to history.
        
        Args:
            operation (str): Description of the operation performed
            result (float): Result of the calculation
        """
        self.history.append(f"{operation}: {result}")
    
    def get_history(self) -> list:
        """
        Instance method to get calculation history.
        
        Returns:
            list: List of calculation history entries
        """
        return self.history.copy() 