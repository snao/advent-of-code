from day4a import *


def test_parse_input():
    inp = "[1518-03-31 00:26] falls asleep"
    ans = parse_input(inp)
    assert ans == [datetime.datetime(1518, 3, 31, 0, 26), "falls asleep"]


def test_parse_action():
    text = "[1518-11-14 23:59] Guard #1069 begins shift"
    text2 = "[1518-05-20 00:02] falls asleep"
    line = parse_input(text)
    ans = parse_action(line)
    assert ans == [59, 0]

def test_update_current_day():
    current_day = np.zeros(15)
    sleep_time = 5
    wake_time = 10
    ans = update_current_day(current_day, sleep_time, wake_time)
    assert np.all(ans == np.array([0., 0., 0., 0., 0., 1, 1, 1, 1, 1, 0., 0., 0., 0., 0.]))


def test_sleepiest_minute():
    array = np.array([[0, 1, 0], [0, 1, 1], [1, 1, 0], [0, 1, 7]])
    ans = sleepiest_minute(array)
    assert ans == 1