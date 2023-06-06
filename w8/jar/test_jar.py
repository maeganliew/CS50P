from jar import Jar
import pytest

test = Jar(30)

def test_init():
    test = Jar(30)
    assert test.capacity == 30
    assert test.size == 0    #initially there's no cookies yet
    with pytest.raises(ValueError):
        test = Jar(-10)


def test_deposit():
    test.deposit(10)
    assert test.size == 10


def test_withdraw():
    test.withdraw(5)
    assert test.size == 5


def test_str():
    #__str__ is basically just converting test into a string, so that i can be printed out
    assert str(test) == 5 * "🍪"