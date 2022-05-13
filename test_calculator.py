"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_substraction(self):
        assert 2 == calculator.substract(4, 2)

    def test_multiply(self):
        assert 100 == calculator.multiply(10, 10)

    def test_division(self):
        assert 3 == calculator.dels(9, 3)
