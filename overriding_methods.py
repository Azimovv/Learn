# you can override methodes inherited from parent classes by redefining it

class Mammal: # defining the parent class
    def __init__(self, name):
        self.hunger = 100
        self.tired = 100
        self.name = name

    def print_result(self, amount, action):
        print("{} {} decreased by {}".format(self.name, action, amount))

    def eat(self, decrease):
        self.hunger -= decrease
        self.print_result(decrease, "hunger")

    def sleep(self, decrease):
        self.tired -= decrease
        self.print_result(decrease, "tiredness")


class Dolphin(Mammal): # child class that inherits the functionality of Mammal
    pass # inheritance without making any changes


class Tiger(Mammal): # inherits but changes functionality of sleep method
    def sleep(self, decrease):
        self.tired -= decrease
        print("The tiger is really tired")


dolphin = Dolphin("dolphin")
dolphin.eat(10)
dolphin.sleep(10)

tiger = Tiger("tiger")
tiger.eat(10)
tiger.sleep(10)

print("\n")

class Tiger(Mammal):
    def sleep(self, decrease):
        super().sleep(decrease)
        print("The tiger is really tired")

# using the super function we can give child class the functionality from
# the parent class's methods without having to retype the functionality
# always try to avoid repeating code with the same functionality in different places when possible
tiger = Tiger("tiger")
tiger.eat(10)
tiger.sleep(10)