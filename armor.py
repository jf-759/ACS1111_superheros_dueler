# armor.py
import random

class Armor:
    def __init__(self, name, max_block):
        '''
        Instantiate instance properties.
        name: String
        max_block: Integer
        '''
        self.name = name
        self.max_block = max_block

    def block(self):
        ''' 
        Return a value between 0 and the value set by self.max_strength.
        '''

        # pick a random value between 0 and self.max_block
        random_value = random.randint(0, self.max_block)
        return random_value
    
if __name__ == "__main__":
    armor1 = Armor('Spidey Sense', 10)
    armor2 = Armor('Kratos\' Shield', 10)

    print(armor1.name)
    print(armor1.block())

    print(armor2.name)
    print(armor2.block())

