# ability.py
import random

class Ability:
    def __init__(self, name, max_damage):
        '''
        Initialize the values passed into this method as instance variables.
        '''

        # Assign the 'name' and 'max_damage'
        # for a specific instance of the Ability class
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        ''' 
        Return a value between 0 and the value set by self.max_damage.
        '''

        # pick a random value between 0 and self.max_damage
        random_value = random.randint(0, self.max_damage)
        return random_value
    
if __name__ == '__main__':

    ability1 = Ability('Web Shooter', 10)
    ability2 = Ability('Thunderstruck', 20)

    print(ability1.name)
    print(ability1.attack())

    print(ability2.name)
    print(ability2.attack())

