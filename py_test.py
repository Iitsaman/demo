import pytest # type: ignore
from main import add, subtract, multiply, divide

def add_test():
    assert add(10,10) == 20

def subtract_test():
    assert subtract(10, 3) == 7

def multiply_test():
    assert multiply(6, 7) == 42

def divide_test():
    assert divide(10, 2) == 5

       