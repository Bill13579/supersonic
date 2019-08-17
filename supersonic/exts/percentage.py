from supersonic.ext import Extension
from supersonic.utils import write, backspace

class Percentage(Extension):
    def __init__(self, digits=1):
        super().__init__()
        self.digits = digits
    
    def stat_update(self, current):
        percentage = round((float(current) / float(self.total)) * 100, self.digits)
        update = ("%." + str(self.digits) + "f") % percentage + "%"
        return update
