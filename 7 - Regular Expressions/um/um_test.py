from um import count

def test_um_on_the_inside():
    assert count("yum") == 0
    assert count("yummy") == 0
    assert count("umab") == 0
    assert count("rum") == 0
    assert count("ummy") == 0
    assert count("umum") == 0
def test_just_um():
    assert count("um") == 1
    assert count("um um") == 2
    assert count("um  um") == 2
    assert count("um, um") == 2
    assert count("um.") == 1
    assert count("um...") == 1
    assert count("um!") == 1
    assert count("um?") == 1
def test_capital_um():
    assert count("UM") == 1
    assert count("YUM") == 0
    assert count("UM!") == 1
    assert count("UM?") == 1
    assert count("UM UM, UM") == 3
    assert count("UM..") == 1
def test_all_cases():
    assert count("Um, thanks for the album.") == 1
    assert count("UM um, um.") == 3
    assert count("UM um yum") == 2
    assert count("this is um, yummy") == 1
    assert count("yummy in my um tummy") == 1
    assert count("UM what this is delicious in my um TUMMY") == 2
