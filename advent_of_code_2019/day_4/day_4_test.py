import pytest
from decode_password import isValidPasswordPart1, isValidPasswordPart2

# Test Values provided in question
def test_case_a():
    assert isValidPasswordPart1('111111') == True


# Test Values provided in question
def test_case_b():
    assert isValidPasswordPart1('223450') == False


# Test Values provided in question
def test_case_c():
    assert isValidPasswordPart1('123789') == False


# Test Values provided in question
def test_case_a():
    assert isValidPasswordPart2('112233') == True


# Test Values provided in question
def test_case_b():
    assert isValidPasswordPart2('123444') == False


# Test Values provided in question
def test_case_c():
    assert isValidPasswordPart2('111122') == True
