from plates import is_valid

def test_too_few_characters():
    assert is_valid("a") == False
    assert is_valid("") == False

def test_too_many_characters():
    assert is_valid("abcdefg") == False

def test_correct_characters():
    assert is_valid("ab") == True
    assert is_valid("abcdef") == True
    assert is_valid("abc") == True

def test_special_characters():
    assert is_valid(".?*&%") == False
    assert is_valid("a.bc") == False
    assert is_valid(".abca") == False
    assert is_valid("abc.") == False
    assert is_valid("abcd") == True

def test_zero_first():
    assert is_valid("0000") == False
    assert is_valid("abc00") == False
    assert is_valid("abc01") == False
    assert is_valid("ab110") == True
    assert is_valid("abc101") == True

def test_middle_numbers():
    assert is_valid("abc1a") == False
    assert is_valid("ab1abc") == False
    assert is_valid("ab123") == True
    assert is_valid("ab1234") == True

def test_starts_with_two_letters():
    assert is_valid("a123") == False
    assert is_valid("ab123") == True
    assert is_valid("1234") == False
    assert is_valid("123abc") == False