from suma import suma


def test_suma():
    assert suma((1, 2, 3)) == 6
    assert suma((1, "2", 3)) == 4
    assert suma([8, 2, 3, 0, 8]) == 21
    assert suma([1, 2.6, "a"]) == 3.6
    assert suma({1: 8, 2: 2, 3: 3, 4: 0, 5: 9}) == 22
    assert suma({1: 8, 2: "a", 3: 3, 4: 0, 5: 9}) == 20


def test_suma_with_cast_to_int():
    assert suma((1, "2", 3), cast_to_int=True) == 6
