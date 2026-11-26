import fuel
import pytest

#test convert
#test str
def test_str():
    with pytest.raises(ValueError):
        fuel.convert("cat")
#test str with /
def test_str_with_slash():
    with pytest.raises(ValueError):
        fuel.convert("cat/hat")
#test float
def test_float():
    with pytest.raises(ValueError):
        fuel.convert("1.2/1.4")
    with pytest.raises(ValueError):
        fuel.convert("1.2/4")
    with pytest.raises(ValueError):
        fuel.convert("3/4.4")
#test one number
def test_one_number():
    with pytest.raises(ValueError):
        fuel.convert("1")
#test no number
def test_nothing():
    with pytest.raises(ValueError):
        fuel.convert("")
#test too many numbers
def test_too_many_numbers():
    with pytest.raises(ValueError):
        fuel.convert("1/2/3")
#test one number and a slash
def test_one_num_and_slash():
    with pytest.raises(ValueError):
        fuel.convert("1/")
#test too large
def test_too_large():
    with pytest.raises(ValueError):
        fuel.convert("5/4")
#test to small
def test_negative_too_small():
    with pytest.raises(ValueError):
        fuel.convert("-1/4")
#test zero division
def test_zero_div():
    with pytest.raises(ZeroDivisionError):
        fuel.convert("1/0")
#test guage
#test e
def test_empty():
    assert fuel.guage(0) == "E"
    assert fuel.guage(1) == "E"
#test f
def test_full():
    assert fuel.guage(99) == "F"
    assert fuel.guage(100) == "F"
#test percent
def test_percent():
    assert fuel.guage(50) == "50%"
    assert fuel.guage(76) == "76%"