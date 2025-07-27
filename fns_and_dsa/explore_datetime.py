from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in a readable format.
    """
    current_date = datetime.now()
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")
    return current_date

def calculate_future_date(current_date, days_to_add):
    """
    Calculate a future date by adding specified days to the current date.
    
    Args:
        current_date: The current datetime object
        days_to_add: Number of days to add (integer)
    
    Returns:
        The future date as a datetime object
    """
    future_date = current_date + timedelta(days=days_to_add)
    return future_date

def main():
    # Part 1: Display current date and time
    current_date = display_current_datetime()
    
    # Part 2: Calculate future date
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        future_date = calculate_future_date(current_date, days_to_add)
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future date: {formatted_future_date}")
    except ValueError:
        print("Error: Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    main() 