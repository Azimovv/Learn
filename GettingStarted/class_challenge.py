class Animals:
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