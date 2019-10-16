class Person:
    def __init__(self):
        self.name = "Bob"

bob = Person()
the_same_bob = bob
print(bob is the_same_bob) # is keyword checks if two objects are the same object (stored in same location in memory)

another_bob = Person()
print(bob is another_bob)