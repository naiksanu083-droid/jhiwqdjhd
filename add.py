# Function to add two numbers
def add_numbers(a, b):
    """
    Add two numbers and return the result.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of a and b
    """
    return a + b


# Example usage
if __name__ == "__main__":
    # Get input from user
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        # Calculate sum
        result = add_numbers(num1, num2)
        
        # Display result
        print(f"The sum of {num1} and {num2} is: {result}")
    
    except ValueError:
        print("Error: Please enter valid numbers")
