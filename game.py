import character
import mechanics
import items

print(True - False)
george = character.Character('George')
print(george.get_stats())
george.add_stats({'strength': 10})
george = mechanics.gen(george)
george.add_level()
george.add_level()
print(george)

george.equip(items.sword_of_crushing)
print(george.equipment['weapon'])

print('Break down the door!')
input('ready?')

# print(roll + mechanics.get_modifier(george.char_stats['strength']))
# mechanics.attack_roll(george, 'simple')
if mechanics.attack(george, george, True) > 3:
    print('The door explodes.')
else:
    print('You broke your foot. Good job asshole.')
