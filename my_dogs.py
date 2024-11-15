import dog

# specify exactly what we want:
my_dog = dog.Dog('Rex', 'SuperDog')
my_dog.bark()

my_other_dog = dog.Dog('Annie', 'SuperDog')
print(my_other_dog.name)

my_third_dog = dog.Dog('Benson', 'SuperDog')
fourth_dog = dog.Dog('Kira', 'Corgi')
fifth_dog = dog.Dog('Mojo', 'Shih Tzu')

# Benson
print(my_third_dog.name)
my_third_dog.bark()

# Kira
print(fourth_dog.name)
fourth_dog.RollOver()

# Mojo 
print(fifth_dog.name)
fifth_dog.Sit()

# Each dog makes the same sound "Woof!" when it barks because we created a method in dog.py that allows which ever dog name you put, to say Woof, when we write it and say something like: my_dog.bark(). 