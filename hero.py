# hero.py
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
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    # fight method:
    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed '''

        if self.starting_health > opponent.starting_health:
            print(f'{self.name} wins the fight against {opponent.name}!')
            
        else:
            self.starting_health < opponent.starting_health
            print(f'{opponent.name} wins the fight against {self.name}!')

if __name__ == "__main__":
    hero1 = Hero("Spiderman", 400)
    hero2 = Hero("Thor", 450)

    hero1.fight(hero2)
