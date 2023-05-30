from numb3rs import validate

def test_default():
    assert validate("1.1.1.1") == True
    assert validate("1.1.1") == False


def test_range():
    assert validate("10.11.12.13") == True
    assert validate("999.1.1.1") == False
    assert validate("1.999.999.999") == False   #important. if validate() only checks for first byte must report error as well