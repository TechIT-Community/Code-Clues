import time

class Animal:
    def __init__(self, name, species, energy):
        self.name = name
        self.species = species
        self.energy = energy

    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name} the {self.species} is eating.")
        time.sleep(2)
        print(f"{self.name} the {self.species} finished eating.")
        self.energy += 15

    def rest(self):
        print(f"{self.name} the {self.species} is resting.")
        time.sleep(3)
        print(f"{self.name} the {self.species} is well-rested.")
        self.energy += 10

class Lion(Animal):
    def make_sound(self):
        return "Roar!"

    def hunt(self):
        print(f"{self.name} the Lion is hunting.")
        time.sleep(2)
        print(f"{self.name} the Lion caught a prey!")
        self.energy += 20

    def roam(self):
        print(f"{self.name} the Lion is roaming the savannah.")
        time.sleep(4)
        print(f"{self.name} the Lion enjoyed the roam.")
        self.energy -= 10

class Elephant(Animal):
    def make_sound(self):
        return "Trumpet!"

    def bathe(self):
        print(f"{self.name} the Elephant is taking a mud bath.")
        time.sleep(3)
        print(f"{self.name} the Elephant is refreshed!")
        self.energy += 15

    def spray_water(self):
        print(f"{self.name} the Elephant is spraying water.")
        time.sleep(2)
        print(f"{self.name} the Elephant had fun spraying water.")
        self.energy -= 8

class Monkey(Animal):
    def make_sound(self):
        return "Ooh oo ah ah!"

    def play(self):
        print(f"{self.name} the Monkey is playing in the trees.")
        time.sleep(2)
        print(f"{self.name} the Monkey had a great playtime!")
        self.energy += 12

    def steal_food(self):
        print(f"{self.name} the Monkey is trying to steal food.")
        time.sleep(1)
        print(f"{self.name} the Monkey successfully stole some food!")
        self.energy += 8


lion = Lion("Leo", "Lion", 112)
elephant = Elephant("Ellie", "Elephant", 127)
monkey = Monkey("Mike", "Monkey", 73)

"""
If the output presented is the following:

A day at the zoo begins...

Leo the Lion is hunting.
Leo the Lion caught a prey!

Mike the Monkey is trying to steal food.
Mike the Monkey successfully stole some food!

Ellie the Elephant is spraying water.
Ellie the Elephant had fun spraying water.

Mike the Monkey is trying to steal food.
Mike the Monkey successfully stole some food!

Ellie the Elephant is spraying water.
Ellie the Elephant had fun spraying water.

Leo the Lion is roaming the savannah.
Leo the Lion enjoyed the roam.

Ellie the Elephant is taking a mud bath.
Ellie the Elephant is refreshed!

Leo the Lion is hunting.
Leo the Lion caught a prey!

Ellie the Elephant is spraying water.
Ellie the Elephant had fun spraying water.

Mike the Monkey is playing in the trees.
Mike the Monkey had a great playtime!

Ellie the Elephant is spraying water.
Ellie the Elephant had fun spraying water.

Mike the Monkey is playing in the trees.
Mike the Monkey had a great playtime!

Find the energy level of each animal after the day at the zoo.
"""