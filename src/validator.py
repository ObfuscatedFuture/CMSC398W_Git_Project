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
