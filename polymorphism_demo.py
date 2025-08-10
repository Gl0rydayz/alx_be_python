import math

class Shape:
    """
    Base class representing a geometric shape.
    
    This class demonstrates the concept of abstract base classes
    where derived classes must implement specific methods.
    """
    
    def area(self):
        """
        Calculate the area of the shape.
        
        This method raises NotImplementedError to indicate that
        derived classes must override this method.
        
        Raises:
            NotImplementedError: This method must be overridden by subclasses
        """
        raise NotImplementedError("Subclasses must override the area() method")
    
    def __str__(self):
        """
        String representation of the shape.
        
        Returns:
            str: The class name of the shape
        """
        return self.__class__.__name__


class Rectangle(Shape):
    """
    Derived class representing a rectangle.
    
    Inherits from Shape and overrides the area method
    to calculate the area of a rectangle.
    """
    
    def __init__(self, length: float, width: float):
        """
        Initialize a Rectangle instance.
        
        Args:
            length (float): The length of the rectangle
            width (float): The width of the rectangle
        """
        self.length = length
        self.width = width
    
    def area(self):
        """
        Calculate the area of the rectangle.
        
        Overrides the base class method to provide
        specific implementation for rectangles.
        
        Returns:
            float: The area of the rectangle (length × width)
        """
        return self.length * self.width
    
    def __str__(self):
        """
        String representation of the rectangle.
        
        Returns:
            str: Detailed information about the rectangle
        """
        return f"Rectangle(length={self.length}, width={self.width})"


class Circle(Shape):
    """
    Derived class representing a circle.
    
    Inherits from Shape and overrides the area method
    to calculate the area of a circle.
    """
    
    def __init__(self, radius: float):
        """
        Initialize a Circle instance.
        
        Args:
            radius (float): The radius of the circle
        """
        self.radius = radius
    
    def area(self):
        """
        Calculate the area of the circle.
        
        Overrides the base class method to provide
        specific implementation for circles.
        
        Returns:
            float: The area of the circle (π × radius²)
        """
        return math.pi * (self.radius ** 2)
    
    def __str__(self):
        """
        String representation of the circle.
        
        Returns:
            str: Detailed information about the circle
        """
        return f"Circle(radius={self.radius})"


# Additional derived class to demonstrate extensibility
class Triangle(Shape):
    """
    Additional derived class representing a triangle.
    
    This class demonstrates how easy it is to extend
    the Shape hierarchy with new shapes.
    """
    
    def __init__(self, base: float, height: float):
        """
        Initialize a Triangle instance.
        
        Args:
            base (float): The base length of the triangle
            height (float): The height of the triangle
        """
        self.base = base
        self.height = height
    
    def area(self):
        """
        Calculate the area of the triangle.
        
        Overrides the base class method to provide
        specific implementation for triangles.
        
        Returns:
            float: The area of the triangle (0.5 × base × height)
        """
        return 0.5 * self.base * self.height
    
    def __str__(self):
        """
        String representation of the triangle.
        
        Returns:
            str: Detailed information about the triangle
        """
        return f"Triangle(base={self.base}, height={self.height})" 