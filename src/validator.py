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

def validate_integer(n):
    """Validate that a number is an integer."""
    try:
        num = float(n)
        return num == int(num)
    except (ValueError, TypeError):
        return False
