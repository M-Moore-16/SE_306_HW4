import pytest
import program.calculator as calculator

class TestAdd:
   
    @pytest.mark.parametrize("a,b,expected", [
        (1, 2, 3),           # positive numbers
        (-2, -4, -6),        # negative numbers
        (0, 5, 5),           # zero case
        (-1, 1, 0),          # mixed signs
        (100, 200, 300),     # larger numbers
    ])
    def test_add(self, a, b, expected):
        assert calculator.Add(a, b) == expected
    
class TestSub:
    
    @pytest.mark.parametrize("a,b,expected", [
        (4, 2, 2),  # Positive numbers
        (-4, 2, -6),  # Negative numbers
        (0, 5, -5),  # Zero case
        (5, -2, 7),  # Mixed case
        (500, 200, 300),  # Large numbers
    ])
    def test_sub(self, a, b, expected):
        assert calculator.Sub(a,b) == expected
        
class TestMulti:
    
    @pytest.mark.parametrize("a,b,expected", [
        (2, 2, 4),  # Positive numbers
        (-4, 2, -8),  # Negative numbers
        (0, 5, 0),  # Zero case
        (5, -2, -10),  # Mixed case
        (100, 100, 10000),  # Large numbers
    ])
    def test_Multi(self, a, b, expected):
        assert calculator.Multi(a,b) == expected
        
class TestDiv:
    
    @pytest.mark.parametrize("a,b,expected", [
        (4, 2, 2),  # Positive numbers
        (-4, 2, -2),  # Negative numbers
        (0, 5, 0),  # Zero case
        (6, -2, -3),  # Mixed case
        (400, 200, 2),  # Large numbers
    ])
    def test_Div(self, a, b, expected):
        assert calculator.Div(a,b) == expected
        
class TestMod:
    
    @pytest.mark.parametrize("a,b,expected", [
        (5, 2, 1),  # Positive numbers
        (-7, 2, 1),  # Negative numbers
        (0, 5, 0),  # Zero case
        (7, -2, -1),  # Mixed case
        (600, 200, 0),  # Large numbers
    ])
    def test_Mod(self, a, b, expected):
        assert calculator.Mod(a,b) == expected

