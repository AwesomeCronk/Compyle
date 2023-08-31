class object:
    def __init__(self, representation):
        self.representation = representation

class constant(object):
    def __init__(self, knownType, representation):
        object.__init__(self, representation)
        self.knownType = knownType

    def __str__(self):
        return 'constant({}, {})'.format(self.knownType, repr(self.representation))
    
    __repr__ = __str__

class variable(object):
    def __init__(self, possibleTypes, representation):
        object.__init__(self, representation)
        self.possibleTypes = possibleTypes

    def __str__(self):
        return 'variable({}, {})'.format(self.possibleTypes, repr(self.representation))
    
    __repr__ = __str__
