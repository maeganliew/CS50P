#import hello function from hello.py
from hello import hello


def test_hello():
    #can use loops to test different values
    assert hello("maegan") == "hello, maegan"
    assert hello() == "hello, world"