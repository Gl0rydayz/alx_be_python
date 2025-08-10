class Book:
    """
    Base class representing a book with common attributes.
    
    This class serves as the foundation for different types of books,
    demonstrating inheritance principles in Python.
    """
    
    def __init__(self, title, author):
        """
        Initialize a Book instance with title and author.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author
    
    def get_info(self):
        """
        Get a string representation of the book's basic information.
        
        Returns:
            str: Formatted string with book title and author
        """
        return f"{self.title} by {self.author}"
    
    def __str__(self):
        """
        String representation method for user-friendly output.
        
        Returns:
            str: Formatted string with book title and author
        """
        return f"{self.title} by {self.author}"


class EBook(Book):
    """
    Derived class representing an electronic book.
    
    Inherits from Book and adds file_size attribute.
    Demonstrates inheritance and method overriding.
    """
    
    def __init__(self, title, author, file_size):
        """
        Initialize an EBook instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            file_size (int): The file size in KB
        """
        # Call the parent class constructor
        super().__init__(title, author)
        self.file_size = file_size
    
    def get_info(self):
        """
        Override the parent method to include file size information.
        
        Returns:
            str: Formatted string with book info and file size
        """
        return f"EBook: {super().get_info()}, File Size: {self.file_size}KB"
    
    def __str__(self):
        """
        String representation method for EBook.
        
        Returns:
            str: Formatted string with EBook information
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """
    Derived class representing a physical printed book.
    
    Inherits from Book and adds page_count attribute.
    Demonstrates inheritance and method overriding.
    """
    
    def __init__(self, title, author, page_count):
        """
        Initialize a PrintBook instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            page_count (int): The number of pages in the book
        """
        # Call the parent class constructor
        super().__init__(title, author)
        self.page_count = page_count
    
    def get_info(self):
        """
        Override the parent method to include page count information.
        
        Returns:
            str: Formatted string with book info and page count
        """
        return f"PrintBook: {super().get_info()}, Page Count: {self.page_count}"
    
    def __str__(self):
        """
        String representation method for PrintBook.
        
        Returns:
            str: Formatted string with PrintBook information
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """
    Library class that demonstrates composition by managing a collection of books.
    
    This class uses composition to store and manage different types of books,
    showcasing how objects can contain other objects.
    """
    
    def __init__(self):
        """
        Initialize an empty library with no books.
        """
        self.books = []
    
    def add_book(self, book):
        """
        Add a book to the library.
        
        Args:
            book (Book): A Book, EBook, or PrintBook instance to add
        """
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("Only Book instances can be added to the library")
    
    def list_books(self):
        """
        Print details of all books in the library.
        
        This method demonstrates polymorphism by calling get_info()
        on different types of book objects.
        """
        if not self.books:
            print("The library is empty.")
            return
        
        print("Books in the library:")
        for book in self.books:
            print(book.get_info())
    
    def get_book_count(self):
        """
        Get the total number of books in the library.
        
        Returns:
            int: The number of books currently in the library
        """
        return len(self.books) 