#same as previous test files, just that this file is now in a folder
from hello import hello


def test_default():
    assert hello() == "hello, world"