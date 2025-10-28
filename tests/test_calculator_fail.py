# tests/test_calculator_fail.py
import pytest
from app.calculator import Calculator

@pytest.mark.xfail(reason="Intentional fail for CI demo")
def test_fail_example():
    calc = Calculator()
    assert calc.add(2, 2) == 5


