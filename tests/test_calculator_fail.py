# tests/test_calculator_fail.py

from app.calculator import Calculator

def test_fail_example():
    calc = Calculator()
    # This is intentionally wrong to demonstrate a failing test
    assert calc.add(2, 2) == 5

