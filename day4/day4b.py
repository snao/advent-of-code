import datetime
import re
import numpy as np


def parse_input(line):
    line = re.sub('[\[\]]', "", line)
    date = line[0:16]
    action = line[17:]
    date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M")
    out = [date, action]
    return out


def parse_action(line):
    entry_time = line[0].minute
    if "falls asleep" in line[1]:
        asleep = 1
    else:
        asleep = 0
    return [entry_time, asleep]


def update_current_day(current_day, sleep_time, wake_time):
    current_day[sleep_time: wake_time] = 1
    return current_day


def sleepiest_minute(array):
    sleepiest_minute = 0
    max_count = 0
    for i in range(0, np.shape(array)[1]):
        current_minute = np.sum(array[:, i])
        if current_minute > max_count:
            max_count = current_minute
            sleepiest_minute = i
    return [max_count, sleepiest_minute]


if __name__ == "__main__":
    with open("day4_input.txt") as f:
        inp = f.read().strip().splitlines()

    entries = []
    guard_table = dict()
    guard_sleep_total = dict()
    guard_id = 0

    for line in inp:
        parsed = parse_input(line)
        entries.append(parsed)
    entries.sort()


    for line in entries:
        action = parse_action(line)
        if "Guard" in line[1]:
            if line == entries[0]:
                guard_id = re.findall(r'\d+', line[1])[0]
                current_day = np.zeros(60)
                guard_table[guard_id] = current_day
            else:
                if guard_id in guard_table:
                    guard_table[guard_id] = np.vstack([guard_table[guard_id], current_day])
                else:
                    guard_table[guard_id] = np.reshape(current_day,[1,60])
                guard_id = re.findall(r'\d+', line[1])[0]
                current_day = np.zeros(60)
        else:
            if action[1] == 1:
                sleep_time = action[0]
            elif action[1] == 0:
                wake_time = action[0]
                current_day = update_current_day(current_day, sleep_time, wake_time)

    for id in guard_table:
        guard_sleep_total[id] = np.sum(guard_table[id])
    sleepiest_guard = max(guard_sleep_total.keys(), key=lambda k: guard_sleep_total[k])

    worst_minute = dict()
    for id in guard_table:
        worst_minute[id] = sleepiest_minute(guard_table[id])
    bad_guard = max(worst_minute.keys(), key=lambda k: worst_minute[k])
    print(worst_minute)
    print(bad_guard)
    print(worst_minute[bad_guard])
