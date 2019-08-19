import supersonic.exts as exts
from supersonic.ext import Extension
from supersonic.utils import write, inplace_write, backspace, UNICODE_SUPPORT

try:
    basestring
except NameError:
    basestring = str

class custom(object):
    def __init__(self, *arrangement, **kwargs):
        total = kwargs.get("total", 100)
        if len(arrangement) == 0:
            raise ValueError("arrangement empty")
        self.arrangement = arrangement
        self.lengths = []
        for a in self.arrangement:
            if isinstance(a, Extension):
                self.lengths.append(0)
                a.conf(total)
            else:
                self.lengths.append(len(a))
        self.__total = total
        self.current = 0
        self.show()

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.done()
    
    @property
    def total(self):
        return self.__total
    
    @total.setter
    def total(self, new_total):
        self.__total = new_total
        for a in self.arrangement:
            if isinstance(a, Extension):
                a.conf(self.__total)

    def __get_update(self):
        s = ""
        for i, arrangement in enumerate(self.arrangement):
            if isinstance(arrangement, Extension):
                update = arrangement.stat_update(self.current)
                self.lengths[i] = len(update)
                s += update
            else:
                s += arrangement
        return s
    
    def show(self):
        inplace_write(self.__get_update(), sum(self.lengths))
    
    def clear(self):
        backspace(sum(self.lengths))
    
    def update(self):
        self.show()
    
    def stat(self, stat):
        if not isinstance(stat, int):
            raise TypeError("stat must be an int")
        self.current = stat
        self.show()
    
    def progress(self, by=1):
        self.stat(self.current + by)
    
    def done(self):
        write("\n")

class supersonic(custom):
    def __init__(self, t="", total=100, pdigits=1, ascii=not UNICODE_SUPPORT, bar_length=15):
        if ascii:
            bar_progress_charset = exts.Bar.CHARSET_NUMERIC
        else:
            bar_progress_charset = exts.Bar.CHARSET_UNICODE_SMOOTH
        bar_placeholder = " "
        super(supersonic, self).__init__(t + " " * min(len(t), 1),
                         exts.Percentage(digits=pdigits),
                         " |",
                         exts.Bar(progress_charset=bar_progress_charset, placeholder=bar_placeholder, length=bar_length),
                         "| ",
                         exts.Fraction(),
                         " [",
                         exts.Eta(),
                         "]",
                         total=total)
sonic = supersonic
