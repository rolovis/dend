#!python3

import interface
import items
import mechanics
import races


class Character(object):
    """Represents a player character.

    Contains functions to add and allocate stats,
    races, classes, skills, and equipment.

    Attributes:
        stats: A dictionary of a Character's attributes
        and their scores.

        equipment: A dictionary of a Character's equipment slots
        and the corresponding equipped item (if any).
        Default value is items.none.

        name: The name of the Character.

        race: The race of the Character. Needs information
        from races.py.

        char_class: The class of the Character. A Character represents
        a classless player character. The gen() function converts a Character
        to its appropriate subclass.

        level: The level of the Character.

        exp: The amount of experience the Character currently has
        towards the next level.

        total_hp: The total amount of hit points the Character has.

        total_mp: The total amount of mana points the Character has.

        hp: The current amount of hit points the Character has.

        mp: The current amount of mana points the Character has.

        base_die: The number of sides a Character's base die is.
        Example: if base_die = 6, the Character rolls 1d6 as his base die."""

    stats = {'strength': 0, 'dexterity': 0, 'constitution': 0,
                  'intelligence': 0, 'wisdom': 0, 'charisma': 0}

    equipment = {'weapon': items.no_weapon, 'chest': items.no_armor,
                      'legs': items.no_armor}
    name = ''
    race = ''

    def __init__(self, name):
        """Initializes a new Character with the given name. Updates
        the amount of hit points the Character has in total.

        Args:
            name: The name of the Character."""
        self.name = name.title()
        self.char_class = ''
        self.level = 1
        self.exp = 0
        self.base_die = 0
        self.total_hp = 0
        self.hp = self.total_hp
        self.hp = self.get_hp()
        self.total_mp = 0
        self.mp = self.total_mp
        self.skills = []
        self.class_skills = []
        self.ac = 0

    def print_modifier(self, stat):
        """Prints an ability score's modifier. Uses the format (-x) and (+x),
        where x is a negative or positive modifier, respectively.

        Args:
            stat: The ability score to retrieve the modifier from.

        Returns:
            '(-x)' if x is a negative modifier and '(x)' otherwise."""
        modifier = mechanics.get_modifier(self.stats[stat])
        if modifier > 0:
            modifier = '+' + str(modifier)
        else:
            modifier = str(modifier)

        return '(' + modifier + ')'

    def get_stats(self):
        """Returns all of a Character's statistics and their respective
        modifiers as a formatted string.

        Returns: A string representing all of the Character's attribute
        scores and modifiers in the format Attribute: Score (Modifier)"""
        stat_string = ''
        for stat, val in sorted(self.stats.items()):
            stat_string += stat.title() + ' : ' + str(val) + ' ' + \
                           self.print_modifier(stat) + '\n'
        return stat_string

    def get_hp(self):
        """Calculates and returns the hit points of a Character using its
        base die value and constitution modifier.

        Returns: The total amount of hit points for the Character."""
        return self.base_die + mechanics.get_modifier(
                       self.stats['constitution'])

    def __str__(self):
        """Generates a formatted string containing a Character's name, level,
        race, class, hit points, mana points, and attribute scores.

        Returns: The formatted string."""
        return '{0} - Level {1}\n{2} | {3}\nHP: {4}   MP: {5}\n\n{6}'.format(
            self.name, self.level, self.race, self.char_class,
            self.hp, self.mp, self.get_stats())

    def add_stats(self, stat_dict):
        """Takes a dictionary of attribute keys and adds their values
        to the Character's attribute scores.

        Args:
            stat_dict: A dictionary where the keys are attributes and the values are
             scores to be added to the Character's attribute scores."""

        for stat, val in stat_dict.items():
            self.stats[stat] += val

    def add_race(self):
        race = input('Enter your race:\n').title()
        try:
            self.add_stats(getattr(races, race).stats)
            self.race = race
        except AttributeError:
            print('Invalid input.')
            self.add_race()

    def add_level(self):
        self.level += 1

    def add_skill(self, name):
        if name in self.class_skills:
            self.skills.append(name)

    def allocate_stats(self):
        points = [8, 10, 12, 13, 14, 15]
        stats = list(self.stats.keys())

        while points:
            print('Points to spend:', points)
            point = int(input())
            if point not in points:
                print('Invalid input.')
                continue

            stat = input('Which stat? Type '
                         '\'help abilities\' for help\n').lower()

            if stat in stats:
                self.stats[stat] += point
                points.remove(point)
                stats.remove(stat)
                print(self.get_stats())
            elif stat == 'help abilities':
                print(interface.help_check(stat))
            else:
                print('Invalid input.')

    def equip(self, equipment):
        equip_type = type(equipment).__name__.lower()
        if equip_type in self.equipment:
            self.equipment[equip_type] = equipment


def add_class(char):
    class_name = input('Enter your class. Type '
                       '\'help classes\' for help\n')

    while class_name == 'help classes':
        print(interface.help_check(class_name))
        class_name = input('Enter your class. Type '
                           '\'help classes\' for help\n')

    try:
        class_name = class_name.title()
        character = globals()[class_name](char)
        character.char_class = class_name
        return character
    except KeyError:
        print('Invalid input.')
        add_class(char)


def gen(char):
    name = input('Enter your name:\n')
    char.name = name
    # char.allocate_stats()
    char.add_stats({'strength': 15})
    char.add_race()
    char = add_class(char)
    return char


class Rogue(Character):

    def __init__(self, char):
        super(Rogue, self).__init__(char.name)
        self.race = char.race
        self.char_class = 'Rogue'
        self.base_die = 8
        self.total_hp = self.get_hp()
        self.hp = self.total_hp
        self.armor_prof = ['light']
        self.class_skills = ['acrobatics', 'athletics', 'deception',
                             'insight', 'intimidation', 'investigation',
                             'perception', 'performance', 'persuasion',
                             'sleight of hand', 'stealth']
        self.weapon_prof = ['simple', 'hand crossbow', 'longsword',
                            'rapier', 'shortsword']
        self.char_throws = ['dexterity', 'intelligence']
        self.skills = []


class Wizard(Character):

    class_skills = ['arcana', 'history', 'insight',
                    'investigation', 'medicine', 'religion']

    def __init__(self, character):
        super(Wizard, self).__init__(character.name)
        self.race = character.race
        self.char_class = 'Wizard'
        self.total_hp = self.get_hp()
        self.hp = self.total_hp
        self.armor_prof = []
        self.weapon_prof = ['dagger', 'dart', 'sling',
                            'quarterstaff', 'light crossbow']

        self.char_throws = ['intelligence', 'wisdom']
        self.base_die = 6
        self.skills = []


class Fighter(Character):

    class_skills = ['acrobatics', 'animal handling', 'athletics',
                    'history', 'insight', 'intimidation',
                    'perception', 'survival']

    def __init__(self, character):
        super(Fighter, self).__init__(character.name)
        self.race = character.race
        self.char_class = 'Fighter'
        self.total_hp = self.get_hp()
        self.hp = self.total_hp
        self.armor_prof = ['light', 'medium', 'heavy']
        self.weapon_prof = ['simple', 'martial']
        self.char_throws = ['strength', 'constitution']
        self.base_die = 10
        self.skills = []


class Cleric(Character):

    class_skills = ['history', 'insight', 'medicine',
                    'persuasion', 'religion']

    def __init__(self, character):
        super(Cleric, self).__init__(character.name)
        self.race = character.race
        self.char_class = 'Cleric'
        self.base_die = 8
        self.total_hp = self.get_hp()
        self.hp = self.total_hp
        self.armor_prof = ['light', 'medium']
        self.weapon_prof = ['simple']
        self.char_throws = ['wisdom', 'charisma']
        self.char_skills = []



