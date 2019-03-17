from day2b import *


def test_str_compare():
    ans = str_compare("abcde", "axcye")
    assert ans == 0


def test_str_compare2():
    ans = str_compare("fghij", "fguij")
    assert ans == 2


def test_remove_index():
    ans = remove_index("asdf", 2)
    assert ans == "asf"
