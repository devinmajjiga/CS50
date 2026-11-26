from twttr import shorten

def test_str():
    assert shorten("What's your name? 1") == "Wht's yr nm? 1"

def test_ints():
    assert shorten("CS50") == "CS50"

def test_special():
    assert shorten("!@#$%^&*()") == "!@#$%^&*()"

def test_none():
    assert shorten("qwrtypsdfghjklzxcvbnm") == "qwrtypsdfghjklzxcvbnm"

def test_all():
    assert shorten("aeiouAEIOU") ==""

def test_nothing():
    assert shorten("") == ""