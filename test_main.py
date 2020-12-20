import pytest
from main import *

def test_mod():
    
    assert Polynomial(4, 4, 1) % Polynomial(2, 1) == Polynomial(0.0)
    assert Polynomial(2, 4, 1, 5) % Polynomial(2, 1, 1) == Polynomial(10.0, -2.0)
                                                                


def test_truediv():
    assert Polynomial(4, 4, 1) / Polynomial(2, 1) == (Polynomial(2.0, 1.0), Polynomial(0.0))
    assert Polynomial(2, 4, 1, 5) / Polynomial(2, 1, 1) == (Polynomial (-4.0, 5.0), Polynomial (10.0, -2.0))
def test_gcd():
    assert Polynomial(4, 4, 1).gcd(Polynomial(2, 1)) == Polynomial(2, 1)
    assert Polynomial(-24, -34, -7, 4, 1).gcd(Polynomial (16, 20, 8, 1)) == Polynomial (8.0, 6.0, 1.0)
