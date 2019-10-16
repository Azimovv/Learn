class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        # __repr__ is a built in method inherited from python's 'Object' parent class
        # this can be overridden to return whatever we want
        return self.name

lion = Lion("Dilbert")
print(lion)

class AlwaysPositive:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return abs(self.number + other.number)

# the AlwaysPositive objects can be used as operands in the expression
# because we defined the __add__ method
# when an addition operator is evaluated, __add__ is called on the first operand object
# and the second operand object is passed into __add__ as a parameter
# it then returns the result of __add__
# because the abs function was used though, it will always return the absolute value of the
# evaluated expression
x = AlwaysPositive(-20)
y = AlwaysPositive(10)

print (x+y)