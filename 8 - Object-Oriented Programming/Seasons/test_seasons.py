from seasons import time_of
from seasons import check_birth
import datetime
import pytest


today = datetime.date.today()


def test_normal_times():
    year_ago = today.replace(year=today.year-1)
    assert time_of(year_ago) == "Five hundred twenty-five thousand, six hundred minutes"
    year_ago = today.replace(year=today.year-2)
    assert time_of(year_ago) == "One million, fifty-one thousand, two hundred minutes"


def test_rejecting_abnormal_times():
    with pytest.raises(ValueError):
        check_birth(birth="")
    with pytest.raises(ValueError):
        check_birth(birth="January 1, 2026")
    with pytest.raises(ValueError):
        check_birth(birth="Jan 1, 2026")
    with pytest.raises(ValueError):
        check_birth(birth="01-01-2026")
    with pytest.raises(ValueError):
        check_birth(birth="20291-01-01")
    with pytest.raises(ValueError):
        check_birth (birth="2026-13-01")
    with pytest.raises(ValueError):
        check_birth(birth="2026-01-32")
    with pytest.raises(ValueError):
        check_birth(birth="0000-00-00")

