import os
from app.calculator import add, subtract

def test_add():
    a = int(os.getenv("A", 2))
    b = int(os.getenv("B", 3))
    assert add(a, b) == a + b

def test_subtract():
    a = int(os.getenv("A", 5))
    b = int(os.getenv("B", 2))
    assert subtract(a, b) == a - b
