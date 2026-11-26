from bank import value

def test_hello():
    assert value("hello") == "0$"
    assert value("Hello") == "0$"
    assert value("HELLO") == "0$"
    assert value("hello, devin") == "0$"

def test_start_h():
    assert value("hi") == "20$"

def test_nothing():
    assert value("1234") == "100$"
    assert value("abcd") == "100$"
    assert value("oh") == "100$"
    assert value("yo hello") == "100$"
    assert value("") == "100$"

