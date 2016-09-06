import character
import mechanics
import items

george = character.Character('George')
print(george.get_stats())
george.add_stats({'strength': 10})
george = character.gen(george)
george.add_level()
george.add_level()
print(george)

george.equip(items.sword_of_crushing)
george.add_skill('acrobatics')
print(george.equipment['weapon'])

print('Break down the door!')
input('ready?')

# if mechanics.attack(george, george, False) > 3:
if mechanics.ability_check(15, 'strength', george):
    print('The door explodes.')
else:
    print('You broke your foot. Good job asshole.')
