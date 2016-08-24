class Item(object):
    def __init__(self):
        self.name = ''


class Pouch(Item):
    def __init__(self):
        super(Pouch, self).__init__()
        self.name = 'Pouch'
        self.storage_space = 5


class Weapon(Item):
    def __init__(self, name, ability, prof,  die):
        super(Weapon, self).__init__()
        self.name = name
        self.ability = ability
        self.prof = prof
        self.die = die
        self.ac = 0

    def __str__(self):
        return '{0}\n{1}d{2} {3}'.format(
            self.name.title(), self.die[0], self.die[1], self.ability.title())


class Armor(Item):
    def __init__(self, name, prof, ac):
        super(Armor, self).__init__()
        self.name = name
        self.prof = prof
        self.ac = ac


# Default values

no_weapon = Weapon('none', 'none', 'none', [1, 1])
no_armor = Armor('none', 'none', 0)

# Weapon list

sword_of_crushing = Weapon('sword of crushing', 'strength', 'simple', [1, 8])
