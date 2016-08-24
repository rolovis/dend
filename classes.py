from character import Character


class Rogue(Character):

    def __init__(self, char):
        super(Rogue, self).__init__(char.name)
        self.race = char.race
        self.char_class = 'Rogue'
        self.base_die = 8
        self.total_hp = self.get_hp()
        self.hp = self.total_hp
        self.armor_prof = ['light']
        self.weapon_prof = ['simple', 'hand crossbow', 'longsword',
                            'rapier', 'shortsword']
        self.char_throws = ['dexterity', 'intelligence']
        self.skills = []
