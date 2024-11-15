# hero.py
from ability import Ability
from armor import Armor
import random

class Hero:
    # we want our hero to have a default 'starting health',
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        '''
        Instance properties:
        aibilities: List
        armors: List
        name: String
        starting_health: Integer
        current_health: Integer
        '''

        # abilities and armors don't have starting values,
        # and are set to empty lists on initialization
        self.abilities = list()
        self.armors = list()

        # assign hero and starting health here:
        self.name = name
        self.starting_health = starting_health

        # current health is the same as starting health 
        # because no damage has been taken yet.
        self.current_health = starting_health

    def add_ability(self, ability):
        '''
        Add ability to abilities list.
        '''

        # we use the append method to add ability objects to our list.
        self.abilities.append(ability)

    def attack(self):
        '''
        Calculate the total damage from all ability attacks.
        return: total_damage:Int
        '''

        # start our total out at 0
        total_damage = 0
        # loop through all our hero's abilities
        for ability in self.abilities:
            # add the damage of each attack to our running total
            total_damage += ability.attack()
        # return the total damage
        return total_damage
            

    # fight method:
    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed '''

        if self.starting_health > opponent.starting_health:
            print(f'{self.name} wins the fight against {opponent.name}!')
            
        else:
            self.starting_health < opponent.starting_health
            print(f'{opponent.name} wins the fight against {self.name}!')

if __name__ == "__main__":

    ability1 = Ability('Web Shooter', 50)
    hero1 = Hero("Spiderman", 400)
    hero1.add_ability(ability1)

    hero2 = Hero("Thor", 450)
    ability2 = Ability('Thunderstruck', 90)
    hero2.add_ability(ability2)

    # print(hero1.abilities)
    # print(hero2.abilities)

    print(hero1.attack())
    print(hero2.attack())


    hero1.fight(hero2)
