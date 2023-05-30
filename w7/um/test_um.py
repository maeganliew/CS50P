from um import count

def test_comma():
    assert count("Hello, um, um, hi") == 2


def test_inwords():
    assert count("yummy") == 0
    assert count("yummy um yummy!") == 1


def test_case():
    assert count("Um, nice") == 1
    assert count("um, nice, Um") == 2
