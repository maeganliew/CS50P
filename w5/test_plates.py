from plates import is_valid


def test_startalpha():
    assert is_valid("CS50") == True
    assert is_valid("50CS") == False


def test_length():
    assert is_valid("a") == False
    assert is_valid("1234567") == False
    assert is_valid("") == False


def test_symbols():
    assert is_valid("CS.!") == False
    assert is_valid("..  ") == False


def test_alphanum():
    assert is_valid("CSCS50") == True
    assert is_valid("CS50CS") == False