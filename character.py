import mechanics
import races


class Character(object):
    char_stats = {'strength': 0, 'dexterity': 0, 'constitution': 0,
                  'intelligence': 0, 'wisdom': 0, 'charisma': 0}

    def __init__(self, name):
        self.char_name = name.title()
        self.char_race = ''
        self.char_class = ''
        self.base_die = 2
        self.char_level = 1
        self.char_exp = 0
        self.char_hp = self.get_hp()
        self.char_mp = 0
        self.char_skills = []

    def print_modifier(self, stat):
        modifier = mechanics.get_modifier(self.char_stats[stat])
        if modifier > 0:
            modifier = '+' + str(modifier)
        else:
            modifier = str(modifier)

        return '(' + modifier + ')'

    def get_stats(self):
        stat_string = ''
        for stat, val in sorted(self.char_stats.items()):
            stat_string += stat.title() + ' : ' + str(val) + ' ' + \
                           self.print_modifier(stat) + '\n'
        return stat_string

    def get_hp(self):
        return self.base_die + mechanics.get_modifier(
                       self.char_stats['constitution'])

    def __str__(self):
        return '%s - Level %s\n%s | %s\nHP: %s  MP: %s\n\n%s' % \
               (self.char_name, self.char_level, self.char_race, self.char_class,
                self.char_hp, self.char_mp, self.get_stats())

    def add_stats(self, stat_dict):
        for stat, val in stat_dict.items():
            self.char_stats[stat] += val

    def add_race(self):
        race = input('Enter your race:\n').title()
        try:
            self.add_stats(getattr(races, race).stats)
            self.char_race = race
        except AttributeError:
            print('Invalid input.')
            self.add_race()

    def add_level(self):
        self.char_level += 1

    def add_skill(self, name):
        self.char_skills.append(name)

    def allocate_stats(self):
        points = [8, 10, 12, 13, 14, 15]
        stats = list(self.char_stats.keys())

        while points:
            print('Points to spend:', points)
            point = int(input())
            if point not in points:
                print('Invalid input.')
                continue

            stat = input('Which stat?\n').lower()

            if stat in stats:
                self.char_stats[stat] += point
                points.remove(point)
                stats.remove(stat)
                print(self.get_stats())
            else:
                print('Invalid input.')


class Rogue(Character):

    def __init__(self, character):
        super(Rogue, self).__init__(character.char_name)
        self.char_race = character.char_race
        self.char_class = 'Rogue'
        self.base_die = 8
        self.char_hp = self.get_hp()
        self.armor_prof = ['light']
        self.weapon_prof = ['simple', 'hand crossbow', 'longsword',
                            'rapier', 'shortsword']
        self.char_throws = ['dexterity', 'intelligence']


class Wizard(Character):

    def __init__(self, character):
        super(Wizard, self).__init__(character.char_name)
        self.char_race = character.char_race
        self.char_class = 'Wizard'
        self.base_die = 6
        self.char_hp = self.get_hp()
        self.armor_prof = []
        self.weapon_prof = ['dagger', 'dart', 'sling',
                            'quarterstaff', 'light crossbow']

        self.char_throws = ['intelligence', 'wisdom']


class Fighter(Character):

    def __init__(self, character):
        super(Fighter, self).__init__(character.char_name)
        self.char_race = character.char_race
        self.char_class = 'Fighter'
        self.base_die = 10
        self.char_hp = self.get_hp()
        self.armor_prof = ['light', 'medium', 'heavy']
        self.weapon_prof = ['simple', 'martial']
        self.char_throws = ['strength', 'constitution']


class Cleric(Character):

    def __init__(self, character):
        super(Cleric, self).__init__(character.char_name)
        self.char_race = character.char_race
        self.char_class = 'Cleric'
        self.base_die = 8
        self.char_hp = self.get_hp()
        self.armor_prof = ['light', 'medium']
        self.weapon_prof = ['simple']
        self.char_throws = ['wisdom', 'charisma']


def add_class(character):
    class_name = input('Enter your class:\n').title()
    character.char_class = class_name
    try:
        character = globals()[class_name](character)
        return character
    except KeyError:
        print('Invalid input.')
        add_class(character)


def gen():
    name = input('Enter your name:\n')
    player = Character(name)
    # player.allocate_stats()
    player.add_stats({'strength': 15})
    player.add_race()
    player = add_class(player)
    return player
