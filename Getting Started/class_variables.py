class Liger:
    """class variables can be accessed without the need to create an object"""
    interests = ["swimming", "eating", "sleeping"]
    def __init__(self, name):
        self.name = name

connor = Liger("Connor")
print(connor.interests)

larry = Liger("Larry")
print(larry.interests)