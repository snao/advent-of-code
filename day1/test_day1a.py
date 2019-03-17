from day1a import *

def test_day1a_parse():
    parsed = day1a_parse("+1\n+1\n+1")
    assert parsed == [1, 1, 1]

def test_day1a_calculate():
    calced = day1a_calculate([1, 1, 1])
    assert calced == 3