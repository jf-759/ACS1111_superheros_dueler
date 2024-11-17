# hero.py
from ability import Ability
from armor import Armor
from weapon import Weapon
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
        self.weapons = list()

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

    def add_weapon(self, weapon):
        '''
        Add weapon to self.abilities
        '''

        self.weapons.append(weapon)

    # armor added:
    def add_armor(self, armor):
        ''' 
        Add armor to self.armors
        Armor: Armor Object
        '''

        self.armors.append(armor)

    # defend method
    def defend(self):
        ''' 
        Calculate the total block amount form all armor blocks.
        return: total_block:Int
        '''
        # start with total at 0
        total_block = 0

        # loop through all hero's abilities
        for armor in self.armors:
            total_block += armor.block()
        
        return total_block

    # attack method
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

        if not self.abilities and not opponent.abilities:
            print('Draw! Neither hero has abilities to fight.')
        
            return

        # while self.is_alive() and opponent.is_alive():
        while True:

            self_damage = self.attack()
            opponent_damage = opponent.attack()

            print(f'{self.name} attacks {opponent.name} for {self_damage} damage!')
            opponent.take_damage(self_damage)

            if not opponent.is_alive():
                print(f'{self.name} wins!')
                break

            print(f'{opponent.name} attacks {self.name} for {opponent_damage} damage!')
            self.take_damage(opponent_damage)

            if not self.is_alive():
                print(f'{opponent.name} wins!')
                break

            if self.is_alive() and opponent.is_alive():
                print('Both heroes are still standing... The battle continues!!! \n')

            if not self.is_alive() and not opponent.is_alive():
                print('It\'s a draw! Both heroes are defeated!')
                break


    def take_damage(self, damage):
        '''
        Updates self.current_health to reflect the damage minus the defense.
        '''

        damage_taken = damage - self.defend()

        if damage_taken > 0:
            self.current_health -= damage_taken
            print(f'{self.name} took {damage_taken} damage!')
        
        else:
            # self.current_health -= damage_taken
            print(f'{self.name} actually gained a little {damage_taken} health!')


    def is_alive(self):
        ''' 
        Return True or False depending on whether the hero is alive or not.
        '''

        print(f'{self.name} has {self.current_health} health left.')

        if self.current_health <= 0:
            print(f'Oh no!! {self.name} has been KO\'ed!')
            return False
        
        else:
            return True





if __name__ == "__main__":

    hero1 = Hero("Spiderman", 400)
    ability1 = Ability('Web Shooter', 50)
    armor1 = Armor('Spidey Sense', 20)
    hero1.add_ability(ability1)
    hero1.add_armor(armor1)

    hero2 = Hero("Thor", 450)
    ability2 = Ability('Thunderstruck', 70)
    armor2 = Armor('Kratos\' Shield', 30)
    weapon2 = Weapon('Mjolnir', 50)
    hero2.add_ability(ability2)
    hero2.add_weapon(weapon2)

    # print(hero2.attack())

    # print(f'{hero1.name} attacks with {ability1.name}!')
    # print(hero1.attack())

    # print(f'{hero2.name} blocks that attack with {armor2.name}!')
    # print(hero2.defend())

    # print(f'{hero2.name} then attacks {hero1.name} with {ability2.name}!')
    # print(hero2.attack())

    # print(f'And {hero1.name} blocks it using {armor1.name}!')
    # print(hero1.defend())

    # print(f'Oh no! {hero1.name} health has gone down!')
    # print(hero1.current_health)


    # hero1.take_damage(150)
    # print(hero1.is_alive())

    # hero1.take_damage(15000)
    # print(hero1.is_alive())


    hero1.fight(hero2)
