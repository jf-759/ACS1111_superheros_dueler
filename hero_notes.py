# hero_notes.py

# You can ignore this page!!!

# ********* This is just a page where I wrote all my notes within each code
# to help me understand what I'm learning better.  *********

import random

class Hero:
    # we want our hero to have a default 'starting health',
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        '''
        Instance properties:
        name: String
        starting_health: Integer
        current_health: Integer
        '''
    # we know the name of our hero, so we assign it here.
    # make sure it is indented so it stays inside the method.
        self.name = name
    # similarly, our starting health is passed in.
        self.starting_health = starting_health
    # when a hero is created, their current health is
    # always the same as their starting health (no damage yet!)
        self.current_health = starting_health

    # fight method:
    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed '''
        # TODO: fight each hero until a victor emerges.
        # winner = random.choice([self, opponent])

        # if winner == self:
        #     print(f'{self.name} wins the fight against {opponent.name}!')
        # else:
        #     print(f'{opponent.name} wins the fight against {self.name}!')

        # Phases to implement:
        # 1. randomly choose winner,
        # hint: look into random library, more specifically the choice method

        if self.starting_health > opponent.starting_health:
            print(f'{self.name} wins the fight against {opponent.name}!')
            
        else:
            self.starting_health < opponent.starting_health
            print(f'{opponent.name} wins the fight against {self.name}!')


# note: because we gave the hero a starting health of 200, it shows up as 200
# even though the default was 100 in the __init__ method.
# if __name__ == '__main__':
#     my_hero = Hero("Grace Hopper", 200)
#     print(my_hero.name)
#     print(my_hero.current_health)
# another note: this block will only run if this script is called directly.
# this will not run if the script is being imported by another script.
# later on, we will want to test our code, in a different file with the Hero import,
# but we won't want to test this code.

if __name__ == "__main__":
    hero1 = Hero("Spiderman", 400)
    hero2 = Hero("Thor", 450)

    hero1.fight(hero2)