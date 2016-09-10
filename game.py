#!python3

import character
import mechanics
import items

player_name = input('Enter your name:\n')
player = character.Character(player_name)
player = character.gen(player)
player.add_stats({'strength': 10})
player.add_level()
player.add_level()
print(player)

player.equip(items.sword_of_crushing)
print(player.equipment['weapon'])

print('Break down the door!')
input('ready?')

if mechanics.ability_check(15, 'strength', player, 'history'):
    print('The door explodes.')
else:
    print('You broke your foot. Good job asshole.')
