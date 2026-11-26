from numb3rs import validate

def test_number_size():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("1.2.3.4") == True
    assert validate("12.34.56.78") == True
    assert validate("145.254.12.8") == True
    assert validate("256.1.2.3") == False
    assert validate("1.256.2.3") == False
    assert validate("1.2.256.3") == False
    assert validate("1.2.3.256") == False
    assert validate("256.256.256.256") == False

def test_number_length():
    assert validate("1.2.3.4") == True
    assert validate("11.22.33.44") == True
    assert validate("123.134.245.255") == True
    assert validate("1.25.234.78") == True
    assert validate("1000.1.2.3") == False
    assert validate("1.1234.1.3") == False
    assert validate("1.1.2000.2") == False
    assert validate("1.2.3.1000") == False
    assert validate("1000.1000.1000.1000") == False

def test_incorrect_inputs():
    assert validate("cat") == False
    assert validate("100") == False
    assert validate("255") == False
    assert validate("000") == False

def test_periods():
    assert validate("1.2.3.4") == True
    assert validate("1.2") == False
    assert validate("1.2.3") == False
    assert validate("1.2.3.4.") == False
    assert validate("1.2.3.4.5") == False
    assert validate("1") == False

def test_preceding_zeroes():
    assert validate("0.0.0.0") == True
    assert validate("1.0.0.0") == True
    assert validate("0.1.0.0") == True
    assert validate("1.2.3.0") == True
    assert validate("00.00.00.00") == False
    assert validate("001.2.3.4") == False
    assert validate("1.02.3.4") == False
    assert validate("1.2.3.04") == False