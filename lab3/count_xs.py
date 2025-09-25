def count_xs(s):
    return s.count("x")


def test_count_xs():
    print("Tester count_xs... ", end="")
    assert 0 == count_xs("foo bar hei")
    assert 1 == count_xs("x")
    assert 4 == count_xs("xxCoolDragonSlayer99xx")
    print("OK")


test_count_xs()
