"""
my_second_project/main.py
A simple Python script demonstrating basic programming concepts.
"""


def greet(name):
    """Return a greeting message for the given name."""
    if not name or not isinstance(name, str):
        raise ValueError("name must be a non-empty string")
    return f"Hello, {name}!"


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def divide(a, b):
    """Return the result of dividing a by b.

    Raises:
        ZeroDivisionError: if b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def main():
    # Greet the user
    print(greet("World"))

    # Basic arithmetic
    result = add(3, 5)
    print(f"3 + 5 = {result}")

    # Safe division
    try:
        print(f"10 / 2 = {divide(10, 2)}")
        print(f"10 / 0 = {divide(10, 0)}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
