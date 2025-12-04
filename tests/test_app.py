from src.app import add


def test_add():
    assert add(3, 3) == 6
    assert add(-1, 1) == 0
