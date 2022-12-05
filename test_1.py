import pytest
from Codec import *

def test_A():
    assert direction("5x5", "FFRFLFLF")

if __name__ == '__main__':
    test_A()
    print("Everything passed")
