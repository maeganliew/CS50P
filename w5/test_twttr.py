from twttr import shorten


def test_lower():
    assert shorten("happy") == "hppy"
    assert shorten("lgbtq") == "lgbtq"


def test_caps():
    assert shorten("HAPPY") == "HPPY"
    assert shorten("LGBTQ") == "LGBTQ"


def test_null():
    assert shorten("") == ""