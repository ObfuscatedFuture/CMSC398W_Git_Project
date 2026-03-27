"""Tests for calculator operations."""
import pytest
from src.validator import validate_integer
from src.calculator import add, subtract, multiply, divide, modulo, factorial
from src.validator import validate_range

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6

def test_divide():
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)

def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120
    assert factorial(3) == 6

def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)

def test_validate_integer():
    assert validate_integer(5) == True
    assert validate_integer(5.0) == True
    assert validate_integer(5.5) == False
    
def test_modulo():
    assert modulo(10, 3) == 1
    assert modulo(7, 2) == 1

def test_modulo_by_zero():
    with pytest.raises(ValueError):
        modulo(5, 0)

def test_range_validation():
    assert validate_range(100) == True
    assert validate_range(2000) == False
    assert validate_range(-2000) == False
