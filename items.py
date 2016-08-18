class Item(object):
    def __init__(self):
        self.name = ''


class Pouch(Item):
    def __init__(self):
        super(Pouch, self).__init__()
        self.name = 'Pouch'
        self.storage_space = 5


class Weapon(Item):
    def __init__(self, name, prof, ability, die):
        super(Weapon, self).__init__()
        self.name = name
        self.prof = prof
        self.ability = ability
        self.die = die


sword_of_crushing = Weapon('Sword of Crushing', 'simple', 'strength')
