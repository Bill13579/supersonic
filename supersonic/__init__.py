import re
import supersonic.exts as exts
from supersonic.ext import Extension
from supersonic.utils import write, inplace_write, backspace
from shutil import get_terminal_size

try:
    basestring
except NameError:
    basestring = str

class custom(object):
    def __init__(self, *arrangement, total=100):
        if len(arrangement) == 0:
            raise ValueError("arrangement empty")
        self.arrangement = arrangement
        self.lengths = []
        for a in self.arrangement:
            if isinstance(a, Extension):
                self.lengths.append(0)
                a.conf(total)
            elif isinstance(a, basestring):
                self.lengths.append(len(a))
            else:
                raise TypeError("only extensions or strings are allowed")
        self.__total = total
        self.current = 0
        self.show()
    
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
        for i in range(len(self.arrangement)):
            arrangement = self.arrangement[i]
            if isinstance(arrangement, Extension):
                update = arrangement.stat_update(self.current)
                self.lengths[i] = len(update)
                s += update
            else:
                s += arrangement
        return s
    
    def show(self):
        last_len = sum(self.lengths)
        inplace_write(self.__get_update(), last_len)
    
    def clear(self):
        backspace(sum(self.lengths))
    
    def update(self):
        self.show()
    
    def stat(self, stat=None):
        if stat is None:
            return self.current
        else:
            if not isinstance(stat, int):
                raise TypeError("stat must be an int")
            self.current = stat
            self.update()
    
    def progress(self, by=1):
        self.stat(self.current + by)
    
    def done(self):
        write("\n")

class supersonic(custom):
    def __init__(self, total=100, pdigits=1, ascii=True, bar_length=15):
        if ascii:
            bar_progress_charset = exts.Bar.CHARSET_NUMERIC
        else:
            bar_progress_charset = exts.Bar.CHARSET_UNICODE_SMOOTH
        bar_placeholder = " "
        super().__init__(exts.Percentage(digits=pdigits),
                         " |",
                         exts.Bar(progress_charset=bar_progress_charset, placeholder=bar_placeholder, length=bar_length),
                         "| ",
                         exts.Fraction(),
                         " [",
                         exts.Eta(),
                         "]",
                         total=total)
sonic = supersonic
