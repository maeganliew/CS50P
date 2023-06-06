from seasons import calculate
import pytest

def test_ValueError():
    with pytest.raises(ValueError):
        calculate("23-14-2020")
    with pytest.raises(ValueError):
        calculate("cat-14-2020")
    with pytest.raises(ValueError):
        calculate("Today is my birthday")


def test_default():
    assert calculate("2022-06-01") == "Five hundred twenty-five thousand, six hundred minutes"
    assert calculate("2021-06-01") == "One million, fifty-one thousand, two hundred minutes"