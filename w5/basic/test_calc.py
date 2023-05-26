from calculator import square   #import the function from calculator.py to test it


def main():
    test_square()


#ASSERTION   to test the calculator fucntion from calculator.py
def test_square():
    try:
        assert square(2) == 4     #like boldly assume? if the function works incorrrectly will have AssertionError
    except AssertionError:    #catch AssertionError and print a more user-friendly error message
        print("2 squared was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")


#  PYTEST  library to automate testing. no need to code so many try/except blocks
#at terminal: $pytest test_c
#divide into different categories to do more number of tests. one test is on one category
import pytest


def test_square():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0


def test_str():
    with pytest.raises(TypeError):     #check if square function will raise TypeError when "cat" is passed
        square("cat")


if __name__ == "__main__":
    main()