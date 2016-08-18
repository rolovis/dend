import random


def coin(num):
    roll = []
    for i in range(num):
        roll.append(random.randint(1, 3))
    return roll


def d4(num):
    roll = []
    for i in range(num):
        roll.append(random.randint(1, 5))
    return roll


def d6():
    return random.randint(1, 7)


def d8():
    return random.randint(1, 9)


def d10():
    return random.randint(1, 11)


def d20():
    return random.randint(1, 21)


def d100():
    return random.randint(1, 101)