from supersonic.ext import Extension

class Total(Extension):
    __slots__ = []
    def __init__(self):
        super(Total, self).__init__()

    def stat_update(self, current):
        return str(self.total)

class Current(Extension):
    __slots__ = []
    def __init__(self):
        super(Current, self).__init__()

    def stat_update(self, current):
        return str(current)

class Fraction(Extension):
    __slots__ = []
    def __init__(self):
        super(Fraction, self).__init__()
    
    def stat_update(self, current):
        return str(current) + "/" + str(self.total)
