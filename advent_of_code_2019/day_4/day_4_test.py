import pytest
from decode_password import isValidPassword

# Test Values provided in question
def test_case_a():
    assert isValidPassword('111111') == True


# Test Values provided in question
def test_case_b():
    assert isValidPassword('223450') == False


# Test Values provided in question
def test_case_c():
    assert isValidPassword('123789') == False
