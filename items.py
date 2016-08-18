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

    def __str__(self):
        return '{0}\n{1}d{2} {3}'.format(
            self.name.title(), self.die[0], self.die[1], self.ability.title())


none = Weapon('none', 'none', 'none', [1, 1])
# Weapon list

sword_of_crushing = Weapon('sword of crushing', 'strength', 'simple', [1, 8])
