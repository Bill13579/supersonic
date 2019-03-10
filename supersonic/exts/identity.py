from supersonic.ext import Extension

class Total(Extension):
    def __init__(self):
        super().__init__()

    def stat_update(self, current):
        return str(self.total)

class Current(Extension):
    def __init__(self):
        super().__init__()

    def stat_update(self, current):
        return str(current)

class Fraction(Extension):
    def __init__(self):
        super().__init__()
    
    def stat_update(self, current):
        return str(current) + "/" + str(self.total)
