"""There are three functions that validate different values. validate_number() returns 
true if the given value can be converted into a float. validate_operation returns true 
if the given value is an operation contained in the valid_ops list. validate_positive() 
returns true if the given value is greater than 0."""

"""Input validation for calculator."""

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

def validate_positive(n):
    """Validate that a number is positive."""
    try:
        num = float(n)
        return num > 0
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