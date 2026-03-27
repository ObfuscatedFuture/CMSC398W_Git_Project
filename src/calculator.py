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
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

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

def modulo(a, b):
    """Return remainder of a divided by b."""
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    return a % b
