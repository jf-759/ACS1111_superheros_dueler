# create a class named Animal
# methods should have def eat and def drink
class Animal:

    def __init__(self, name):
        self.name = name

    # eat method should print animal's name and 'is eating.'
    def eat(self):
        print(f'{self.name} is eating.')
    
    # drink method should print the animal's name and 'is drinking.'
    def drink(self):
        print(f'{self.name} is drinking.')

# once you do that, in the same file, create the Frog class (a subclass of Animal)
#   frog class should have def jump method 
#   frog class should also print frog's name and 'is jumping.'  
class Frog(Animal):
    
    def jump(self):
        print(f'{self.name} is jumping!')

# Test your code by instantiating one Animal and one Frog
#   --> make sure that your Frog object can eat, drink, and jump
#   --> and that your Animal can eat and drink

the_frog = Frog('Kerropi')
the_frog.eat()
the_frog.drink()
the_frog.jump()




# my choice for animal:

class Otter(Animal):
    
    def eat(self):
        print(f'{self.name} is eating.')

    def drink(self):
        print(f'{self.name} is drinking.')
        
the_otter = Otter('Otis')
the_otter.eat()
the_otter.drink()




