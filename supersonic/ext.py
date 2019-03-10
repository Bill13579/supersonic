import time
import supersonic

class Extension(object):
    def __init__(self):
        self.total = 0
    
    def conf(self, total):
        self.total = total

    def stat_update(self, current):
        pass

def test(ext, total=1000, sleep_time=0.01):
    p = supersonic.custom(ext, total=total)
    for i in range(total):
        p.progress()
        time.sleep(sleep_time)
    p.done()
