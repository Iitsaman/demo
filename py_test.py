import pytest # type: ignore
from main import add, subtract, multiply, divide

def test_add():
    assert add(10, 10) == 20

def test_subtract():
    assert subtract(10, 3) == 7

def test_multiply():
    assert multiply(6, 7) == 42

def test_divide():
    assert divide(10, 2) == 5

       