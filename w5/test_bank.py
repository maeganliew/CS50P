from bank import value


def test_h():
    assert value("heyyy") == 20


def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0


def test_random():
    assert value("yamada") == 100
    assert value("") == 100