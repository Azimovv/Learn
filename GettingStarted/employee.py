class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first = first_name
        self.last = last_name
        self.salary = salary

    def give_raise(self, raise_amount=''):
        if raise_amount:
            self.salary += raise_amount
        else:
            self.salary += 5000
