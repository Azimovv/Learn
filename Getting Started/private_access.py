# python does not have private variables
# instead convention is to precede the variable name with an underscore
# this lets other programmers know not to use it, or use it at their own risk

class PublicPrivateExample:
    def __init__(self):
        self.public_variable = "Callers know they can access this"
        self._dontusethisvariable = "Callers know they shouldn't access this"
    def public_method(self):
        # callers know they can use this method
        pass
    def _dont_use_this_method(self):
        # callers know they shouldn't use this method
        pass