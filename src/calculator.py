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
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
 

 #Random comment for commit experiment

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
