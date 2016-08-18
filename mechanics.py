import math
import random


skill_list = {'athletics': 'strength', 'acrobatics': 'dexterity',
              'sleight of hand': 'dexterity', 'stealth': 'dexterity',
              'arcana': 'intelligence', 'history': 'intelligence',
              'investigation': 'intelligence', 'nature': 'intelligence',
              'religion': 'intelligence', 'survival': 'wisdom',
              'animal handling': 'wisdom', 'insight': 'wisdom',
              'medicine': 'wisdom', 'perception': 'wisdom',
              'deception': 'charisma', 'performance': 'charisma',
              'intimidation': 'charisma', 'persuasion': 'charisma'}

# skill_modifier(skill): if skill in char.skill_list:
#       roll += character.get_proficiency(char.level)


def check(dc, score):
    return True if score >= dc else False


def roll(die_num, die_size):
    random.seed()
    roll_list = []
    for i in range(die_num):
        roll_list.append(random.randint(1, die_size))
    return roll_list


def attack_roll(char, weapon):
    roll_list = roll(char.char_level, char.base_die)
    for die in roll_list:
        print(die, end=', ')
    attack = sum(roll_list)
    if weapon in char.weapon_prof:
        bonus = get_proficiency(char.char_level)
        attack += bonus
        print('(+%s)' % str(bonus), end=' = ')
    attack += char.get_modifier(char.stats_list[weapon.prof])
    print('%s' % str(attack))
    return attack


def get_modifier(level):
    return math.floor((level - 10) / 2)


def get_proficiency(level):
    return math.ceil(level / 4) + 1
