from random import randint

class Animals:
    """Class to hold different types of animals"""
    def __init__(self, name, coldBlooded, eggs, trait):
        self.is_coldBlooded = coldBlooded
        self.eggs = eggs
        self.trait = trait
        self.name = name
        self.print_result()

    def print_result(self):
        print("The {} {} {} and can {}".format(self.name, self.eggs, self.is_coldBlooded, self.trait))


crocodile = Animals("Crocodile", "is cold blooded", "lays eggs", "exert large amounts of bite pressure")
print('\n')

human = Animals("Human", "is warm blooded", "gives live birth", "exhibit self awareness")
print('\n')

frog = Animals("Frog", "is cold blooded", "lays eggs", "live in water and on land")
print('\n')

eagle = Animals("Eagle", "is warm blooded", "lays eggs", "fly")

class Die():
    """Create a Die of a number of sides decided by the user
    and roll it with the method roll_die"""
    def __init__(self, sides):
        self.sides = sides
    def roll_die(self):
        print(randint(1,self.sides))

six_sided = Die(6)
ten_sided = Die(10)
twenty_sided = Die(20)

for num in range(10):
    six_sided.roll_die()

print("")

for num in range(10):
    ten_sided.roll_die()

print("")

for num in range(10):
    twenty_sided.roll_die()