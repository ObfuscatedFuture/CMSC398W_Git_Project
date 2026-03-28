"""Basic calculator operations."""
import math
"""
This module provides arithmetic operations for a calculator.

It includes functions for:
- Standard arithmetic: addition, subtraction, multiplication, and division.
- Specialized arithmetic: modulo operation for finding remainders.
- Error handling: validates inputs to prevent division or modulo by zero.

Each operation includes debug logging to track the execution flow.
"""

"""Hi I was here"""
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
    if b != 0:
        result = a / b
    else:
        raise ValueError("Cannot divide by zero")
    
    return result

def square_root(a):
    """Calculate square root of a."""
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(a)

def power(a, b):
    """Raise a to the power of b."""
    result = a ** b
    return result

def factorial(n):
    """Calculate factorial of n."""
    if n < 0:
        raise ValueError("Cannot calculate factorial of negative number")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def modulo(a, b):
    """Return remainder of a divided by b."""
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    return a % b
