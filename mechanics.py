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


def attack_roll(char):
    weapon = char.char_equipment['weapon']
    roll_list = roll(char.char_level, char.base_die)

    # print base roll
    for die in roll_list:
        print(die, end=', ')

    # add weapon roll
    roll_list.extend(roll(weapon.die[0], weapon.die[1]))
    print('(+{0})'.format(roll_list[len(roll_list) - 1]), end=' ')
    attack = sum(roll_list)

    # add proficiency bonus if applicable
    if weapon.prof in char.weapon_prof:
        bonus = get_proficiency(char.char_level)
        attack += bonus
        print('(+{0})'.format(bonus), end=' = ')

    # ???
    attack += get_modifier(char.weapon_prof.index(weapon.prof))


    print('%s' % str(attack))
    return attack


def get_modifier(level):
    return math.floor((level - 10) / 2)


def get_proficiency(level):
    return math.ceil(level / 4) + 1
