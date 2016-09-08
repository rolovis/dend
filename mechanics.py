import math
import random

# test twat

skill_list = {'athletics': 'strength', 'acrobatics': 'dexterity',
              'sleight of hand': 'dexterity', 'stealth': 'dexterity',
              'arcana': 'intelligence', 'history': 'intelligence',
              'investigation': 'intelligence', 'nature': 'intelligence',
              'religion': 'intelligence', 'survival': 'wisdom',
              'animal handling': 'wisdom', 'insight': 'wisdom',
              'medicine': 'wisdom', 'perception': 'wisdom',
              'deception': 'charisma', 'performance': 'charisma',
              'intimidation': 'charisma', 'persuasion': 'charisma'}


def check(dc, score):
    return True if score >= dc else False


def ability_check(dc, ability, character, skill=''):
    """Determines whether a given skill check succeeds.

    skill_check takes a difficulty score, the skill associated with the roll.
    If the given Character has proficiency in that skill, the proficiency score
    for that Character is added to the total roll. The roll is then checked
    against the difficulty score using the check function.

    Args:
        dc: The difficulty level of the skill check.

        skill: The skill associated with the check.

        character: The Character performing the check.

    Returns:
        True if the character's score is greater than or equal to
        the given difficulty score, and False otherwise."""

    score = sum(roll(1, 20)) + get_modifier(character.stats[ability])
    print(score)
    if skill in character.skills:
        score += get_proficiency(character.level)
    print(dc, score)
    return check(dc, score)


def roll(die_num, base_die):
    random.seed()
    roll_list = []
    for i in range(die_num):
        roll_list.append(random.randint(1, base_die))
    return roll_list


def attack(enemy, char, defender):
    damage = 0
    weapon = char.equipment['weapon']
    if check(char.equipment['chest'].ac, attack_roll(char)):
        damage = sum(roll(weapon.die[0], weapon.die[1]))
        enemy.hp -= damage
        print('Took' if defender else 'Did', end=' ')
        print('{0} damage!'.format(damage))
        return damage


def attack_roll(char):
    weapon = char.equipment['weapon']
    roll_list = roll(char.level, char.base_die)
    final_roll = sum(roll_list)

    # print base roll
    for die in roll_list:
        print(die, end=' ')

    # add proficiency bonus if applicable
    if weapon.prof in char.weapon_prof:
        bonus = get_proficiency(char.level)
        final_roll += bonus
        print('(+{0})'.format(bonus), end=' = ')

    print('{0}'.format(final_roll))
    return final_roll


def get_modifier(score):
    """Calculates and returns the ability modifier for the given score."""

    return math.floor((score - 10) / 2)


def get_proficiency(level):
    """Calculates and returns a Character's proficiency bonus
    based on the Character's level."""

    return math.ceil(level / 4) + 1

