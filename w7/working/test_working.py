from working import convert
import pytest  #to check if any errors raised


def test_amtopm():
    assert convert("5:00 AM to 9:00 PM") == "05:00 to 21:00"


def test_pmtoam():
    assert convert("5:00 PM to 9:00 AM") == "17:00 to 09:00"


def test_valueerorr():
    with pytest.raises(ValueError):
        convert("cat:dog AM to dog:cat PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 10:90 PM")
    with pytest.raises(ValueError):     #when user omits "to"
        convert("9 AM 10 PM")