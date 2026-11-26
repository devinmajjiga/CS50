import pytest
from working import convert

def test_invalid_inputs():
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("9 - 5")
    with pytest.raises(ValueError):
        convert("9 too 5")
    with pytest.raises(ValueError):
        convert("9:000 to 5:000")
    with pytest.raises(ValueError):
        convert("9:60 to 5:60")
    with pytest.raises(ValueError):
        convert("13:60 to 17:60")
#done

def test_am_to_pm():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:32 AM to 5:23 PM") == "09:32 to 17:23"
def test_pm_to_am():
    assert convert("9:00 PM to 5:00 AM") == "21:00 to 05:00"
    assert convert("9:59 PM to 5:22 AM") == "21:59 to 05:22"
def test_am_to_am():
    assert convert("1:00 AM to 9:00 AM") == "01:00 to 09:00"
    assert convert("1:35 AM to 9:55 AM") == "01:35 to 09:55"
def test_pm_to_pm():
    assert convert("5:00 PM to 9:00 PM") == "17:00 to 21:00"
    assert convert("5:49 PM to 9:34 PM") == "17:49 to 21:34"
def tets_reset_to_0():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12:12 AM to 12:21 PM") == "00:12 to 12:21"