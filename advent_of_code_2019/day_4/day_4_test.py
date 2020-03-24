from decode_password import isValidPasswordPart1, isValidPasswordPart2


# Test Values provided in question
def test_case_a():
    assert isValidPasswordPart1('111111') is True


# Test Values provided in question
def test_case_b():
    assert isValidPasswordPart1('223450') is False


# Test Values provided in question
def test_case_c():
    assert isValidPasswordPart1('123789') is False


# Test Values provided in question
def test_case_d():
    assert isValidPasswordPart2('112233') is True


# Test Values provided in question
def test_case_e():
    assert isValidPasswordPart2('123444') is False


# Test Values provided in question
def test_case_f():
    assert isValidPasswordPart2('111122') is True
