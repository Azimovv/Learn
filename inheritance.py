class Adult:
    def __init__(self, name, height, weight, eye_color):
        self.name = name
        self.height = height
        self.weight = weight
        self.eye_color = eye_color
    def print_name(self):
        print(self.name)

class Kid(Adult):
    # Inheritance, can take a parent class's variables and methods and pass them to a child
    def print_cartoon (self, favorite_cartoon):
        print("{}'s favorite cartoon is {}".format(self.name, favorite_cartoon))


tom = Adult("Tom", 6, 190, "brown")

print(tom.name)
print(tom.height)
print(tom.weight)
print(tom.eye_color)
tom.print_name()

child = Kid("Lauren", 3, 50, "blue")
print(child.name)
print(child.height)
print(child.weight)
print(child.eye_color)
child.print_name()
child.print_cartoon('Duck Tales')