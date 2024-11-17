# team.py
import random

class Team:
    def __init__(self, name):
        '''
        Initialize your team with its team name and an empty list of heroes
        '''

        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        ''' 
        Remove hero from heroes list.
        If Hero isn't found return 0
        '''

        foundHero = False

        # loop through each hero in our list
        for hero in self.heroes:
            # if we find them, remove them from the list
            if hero.name == name:
                self.heroes.remove(hero)
                # set our indicator to True
                foundHero = True

        # if we looped through our list and did not find our hero, 
        # the indicator would have never changed, so return 0

        if not foundHero:
            return 0
        
    def view_all_heroes(self):
        '''
        Prints out all heroes to the console.
        '''

        # TODO: loop over the list of heroes and print their names to the terminal one by one.

        for hero in self.heroes:
            print(f'Hero name: {hero.name}')

    def add_hero(self, hero):
        ''' 
        Add Hero object to self.heroes.
        '''

        # TODO: add the Hero object that is passed in to the list of heroes in
        # self.heroes

        self.heroes.append(hero)

    def stats(self):
        '''
        Print team statistics.
        '''

        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print(f'{hero.name} Kill/Deaths: {kd}')

    def revive_heroes(self, health=100):
        '''
        Reset all heroes health to starting_health.
        '''

        # TODO: for each hero in self.heroes, set the hero's current health to their starting health

        for hero in self.heroes:
            hero.current_health = hero.starting_health
            print(f'{hero.name} has been revived to {hero.starting_health} health!')

    def attack(self, other_team):
        '''
        Battle each team against each other.
        '''

        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:

            hero = random.choice(living_heroes)
            opponent = random.choice(living_opponents)

            hero.fight(opponent)

            if hero.current_health < 0:
                living_heroes.remove(hero)
                print(f'{hero.name} has fallen!')

            elif opponent.current_health < 0:
                living_opponents.remove(opponent)
                print(f'{opponent.name} has fallen!')

            else:
                pass



