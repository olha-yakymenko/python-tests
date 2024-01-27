from plikstepik import dodaj


def test1():
    assert dodaj(2, 5) == 2 + 5


def test2():
    assert dodaj(-2, 8) == -2 + 8


def test3():
    assert dodaj(3, -4) == 3 - 4


def test4():
    assert dodaj(-1, -1) == -1 - 1