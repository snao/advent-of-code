from day2a import *

def test_parse_1():
    ans = parse_1("abcccd")
    assert ans == 0


def test_parse_1_2():
    ans = parse_1("bababc")
    assert ans == 1


def test_parse_2_1():
    ans = parse_2("abcdef")
    assert ans == 0


def test_parse_2_2():
    ans = parse_2("abcccd")
    assert ans == 1
