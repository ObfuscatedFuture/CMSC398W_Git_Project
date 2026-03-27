"""
This module provides arithmetic operations for a calculator.

It includes functions for:
- Standard arithmetic: addition, subtraction, multiplication, and division.
- Specialized arithmetic: modulo operation for finding remainders.
- Error handling: validates inputs to prevent division or modulo by zero.

Each operation includes debug logging to track the execution flow.
"""

def add(a, b):
    """Add two numbers."""
    print(f"[DEBUG] Adding {a} + {b}")
    result = a + b
    print(f"[DEBUG] Result: {result}")
    return result

def subtract(a, b):
    """Subtract b from a."""
    print(f"[DEBUG] Subtracting {a} - {b}")
    result = a - b
    print(f"[DEBUG] Result: {result}")
    return result

def multiply(a, b):
    """Multiply two numbers."""
    print(f"[DEBUG] Multiplying {a} * {b}")
    result = a * b
    print(f"[DEBUG] Result: {result}")
    return result

def divide(a, b):
    """Divide a by b."""
    print(f"[DEBUG] Dividing {a} / {b}")
    if b == 0:
        print(f"[DEBUG] Error: Division by zero!")
        raise ValueError("Cannot divide by zero")
    result = a / b
    print(f"[DEBUG] Result: {result}")
    return result

def power(a, b):
    """Raise a to the power of b."""
    result = a ** b
    return result

# hello
    return a / b

def modulo(a, b):
    """Return remainder of a divided by b."""
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    return a % b
