import pytest
import calculator

# test multiplication and addition integration        
class TestMultiAndAdd:
    
    @pytest.mark.parametrize("a,b,expected", [
        (5, 5, 30),  # Positive numbers
        (-7, 2, -12),  # Negative numbers
        (0, 5, 5),  # Zero case
        (7, -2, -16),  # Mixed case
    ])
    def test_multi_and_add(self, a, b, expected):
        assert calculator.Add(calculator.Multi(a,b),b) == expected
        
# test multiplication and addition integration        
class TestDivAndSub:
    
    @pytest.mark.parametrize("a,b,expected", [
        (20, 5, -1),  # Positive numbers
        (-8, 2, -6),  # Negative numbers
        (0, 5, -5),  # Zero case
        (12, -2, -5),  # Mixed case
    ])
    def test_div_and_sub(self, a, b, expected):
        assert calculator.Sub(calculator.Div(a,b),b) == expected