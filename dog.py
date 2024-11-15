class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        print('dog initialized!')

    # methods are defined as their own named functions inside the class
    # everytime you make a class method, input the 'self' parameter

    def bark(self):
        print('Woof!')

    def RollOver(self):
        print('Roll over!')

    def Sit(self):
        print('Sit!')

# instsantiation call that creates a Dog object:
# --> Dog('Rex') <--

# assigning it to the value of the my_dog variable.


# print(my_dog) # <--- This will print <__main__.Dog object at 0x1011d6bd0> which is its dog class.
# print(my_dog.name) # this will print its name 'Rex'

# should print 'SuperDog'
# print(my_dog.breed)