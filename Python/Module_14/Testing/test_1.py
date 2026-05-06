def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, -3) == -4

def test_add_big_numbers():
    assert add(2000000, 3000000) == 5000000