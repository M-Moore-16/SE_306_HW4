import pytest
from program import calculator
# test Multiplication and Addition integration        
class TestMultiAndAdd:
    
    @pytest.mark.parametrize("a,b,expected", [
        (5, 5, 30),  # Positive numbers
        (-7, 2, -12),  # Negative numbers
        (0, 5, 5),  # Zero case
        (7, -2, -16),  # Mixed case
    ])
    def test_multi_and_add(self, a, b, expected):
        assert calculator.Add(calculator.Multi(a,b),b) == expected
        
# test Division and Subtraction integration        
class TestDivAndSub:
    
    @pytest.mark.parametrize("a,b,expected", [
        (20, 5, -1),  # Positive numbers
        (-8, 2, -6),  # Negative numbers
        (0, 5, -5),  # Zero case
        (12, -2, -4),  # Mixed case
    ])
    def test_div_and_sub(self, a, b, expected):
        assert calculator.Sub(calculator.Div(a,b),b) == expected
        
class TestModAndMulti:
    
    @pytest.mark.parametrize("a,b,c, expected", [
        (5, 4, 2, 0), # Positive numbers
        (-3, 3, 2, 1), # Negative numbers
        (1, 0, 1, 0), # Zero case
        (-1, -1, 1, 0), # Mixed case
    ])
    def test_Mod_and_multi(self, a, b, c, expected):
        assert calculator.Mod(calculator.Multi(a,b), c) == expected