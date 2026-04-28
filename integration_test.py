import pytest
import calculator

# test multiplication and addition integration        
class TestTogether:
    
    @pytest.mark.parametrize("a,b,expected", [
        (5, 5, 30),  # Positive numbers
        (-7, 2, -12),  # Negative numbers
        (0, 5, 5),  # Zero case
        (7, -2, -16),  # Mixed case
    ])
    def test_together(self, a, b, expected):
        assert calculator.Add(calculator.Multi(a,b),b) == expected