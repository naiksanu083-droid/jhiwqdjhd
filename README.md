# Method 1: Direct addition
num1 = 10
num2 = 20
sum = num1 + num2
print(f"The sum of {num1} and {num2} is {sum}")

# Method 2: Using user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sum = num1 + num2
print(f"The sum is {sum}")

# Method 3: Using a function
def add_two_numbers(a, b):
    return a + b

result = add_two_numbers(15, 25)
print(f"Result: {result}")
