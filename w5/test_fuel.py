from fuel import convert, gauge
import pytest   #to check if errors are raised


def test_convert():
    assert convert("2/8") == 25
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("3/2")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"


#if check percentage >100 in gauge function and test like below:
#    with pytest.raises(ValueError):
#        gauge(120)

#will not pass CS50's check. not sure why