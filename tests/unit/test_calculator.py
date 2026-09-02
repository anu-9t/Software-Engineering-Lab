"""
Unit Tests for Calculator
Students start with 2 passing tests, then add more
"""

import pytest
from src.calculator import add, divide, subtract, multiply, power, sqrt


class TestBasicOperations:
    """Test basic arithmetic operations"""

    def test_add_positive_numbers(self):
        """Test adding positive numbers"""
        assert add(2, 3) == 5
        assert add(10, 15) == 25

    def test_add_negative_numbers(self):
        """Test adding negative numbers"""
        assert add(-1, -1) == -2
        assert add(-5, 3) == -2

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers"""
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6

    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers"""
        assert subtract(-1, -1) == 0
        assert subtract(-5, -3) == -2


class TestMultiplyDivideWithValidation:
    """Test multiplication and division with input validation."""

    def test_multiply_input_validation(self):
        """Test multiply rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply("5", 3)
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply(5, "3")

    def test_divide_input_validation(self):
        """Test divide rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Division requires numeric inputs"):
            divide("10", 2)


# TODO: Students will add TestMultiplyDivide class
class TestMultiplyDivide:
    """Test multiplication and division arithmetic"""

    def test_multiply_numbers(self):
        """Test multiplying numbers"""
        assert multiply(3, 4) == 12
        assert multiply(-2, 3) == -6

    def test_divide_numbers(self):
        """Test dividing numbers"""
        assert divide(10, 2) == 5
        assert divide(9, 3) == 3

    def test_divide_by_zero(self):
        """Test dividing by zero raises ValueError"""
        with pytest.raises(ValueError, match="Cannot divide"):
            divide(10, 0)


class TestAdvancedOperations:
    """Test power and square root operations with validation."""

    def test_power_numbers(self):
        """Test power calculation"""
        assert power(2, 3) == 8
        assert power(5, 0) == 1
        assert power(2, -1) == 0.5

    def test_power_input_validation(self):
        """Test power rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            power("2", 3)
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            power(2, "3")

    def test_sqrt_numbers(self):
        """Test square root calculation"""
        assert sqrt(16) == 4
        assert sqrt(0) == 0
        assert sqrt(2.25) == 1.5

    def test_sqrt_negative(self):
        """Test square root of negative numbers raises ValueError"""
        with pytest.raises(ValueError, match="Cannot calculate square root"):
            sqrt(-4)

    def test_sqrt_input_validation(self):
        """Test sqrt rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Input must be a number"):
            sqrt("16")
