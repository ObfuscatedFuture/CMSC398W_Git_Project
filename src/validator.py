"""
This file has three validation functions. The first one, validate_number, will
check that a given value can be converted into a number. The second function, 
validate_operation, will check that a given operation is accepted by the
calculator. The third function, validate_non_negative, will check that a given
number is positive.
"""

def validate_number(value):
    """Validate that value can be converted to a number."""
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False

def validate_operation(op):
    """Validate that operation is supported."""
    valid_ops = ['+', '-', '*', '/']
    return op in valid_ops

def validate_non_negative(n):
    """Validate that a number is non-negative."""
    try:
        num = float(n)
        return num >= 0
    except (ValueError, TypeError):
        return False
  
def validate_positive(n):
    """Validate that a number is positive."""
    try:
        num = float(n)
        return num > 0
      
def validate_integer(n):
    """Validate that a number is an integer."""
    try:
        num = float(n)
        return num == int(num)
    except (ValueError, TypeError):
        return False
    
def validate_range(value, min_val=-1000, max_val=1000):
    """Validate that number is within acceptable range."""
    try:
        num = float(value)
        return min_val <= num <= max_val
    except (ValueError, TypeError):
        return False

def is_positive(n):
    # Added this comment for checkpoint 4 step 2
    """Check if a number is positive."""
    return n > 0
