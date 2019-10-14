class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner


class Person:
    def __init__(self, name):
        self.name = name


mick = Person("Mick Jagger")
dog = Dog("Sir Boofington the 3rd", "German Shepard", mick.name)

print(dog.name)
print(dog.breed)
print(dog.owner)

class Orange:
    def __init__(self, color, brand, firmness):
        self.color = color
        self.brand = brand
        self.firmness = firmness

orange = Orange("orange", "publix", True)
print(orange.color)
print(orange.brand)
print(orange.firmness)