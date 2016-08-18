import character
import mechanics

print(True - False)
george = character.Character('George')
print(george.get_stats())
george = character.gen()
george.add_level()
george.add_level()
print(george)

print('Break down the door!')
input('ready?')

# print(roll + mechanics.get_modifier(george.char_stats['strength']))
# mechanics.attack_roll(george, 'simple')
if mechanics.check(15, mechanics.attack_roll(george, 'simple')):
    print('The door explodes.')
else:
    print('You broke your foot. Good job asshole.')
