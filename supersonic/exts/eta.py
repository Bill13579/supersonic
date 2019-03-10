import time
from datetime import timedelta
from supersonic.ext import Extension

def n2dhms(nanoseconds):
    days, nanoseconds = divmod(nanoseconds, 1e9*60*60*24)
    days, nanoseconds = int(days), int(nanoseconds)

    hours, nanoseconds = divmod(nanoseconds, 1e9*60*60)
    hours, nanoseconds = int(hours), int(nanoseconds)

    minutes, nanoseconds = divmod(nanoseconds, 1e9*60)
    minutes, nanoseconds = int(minutes), int(nanoseconds)

    seconds, nanoseconds = divmod(nanoseconds, 1e9)
    seconds, nanoseconds = int(seconds), int(nanoseconds)

    return days, hours, minutes, seconds

class Eta(Extension):
    def __init__(self, alpha=4):
        super().__init__()
        self.records = []
        self.last = None
        self.alpha = alpha
    
    def stat_update(self, current):
        s = "eta "
        t = round(time.time() * 1e9)
        if self.last is None:
            s += "--"
        else:
            if len(self.records) >= self.alpha:
                del self.records[0]
            self.records.append(t - self.last)
            average_time = int(float(sum(self.records)) / float(len(self.records)))
            remaining_time = average_time * (self.total - current)
            days, hours, minutes, seconds = n2dhms(remaining_time)
            if days != 0:
                s += str(days) + "d "
            if hours != 0:
                s += str(hours) + "h "
            if minutes != 0:
                s += str(minutes) + "m "
            s += str(seconds) + "s"
        self.last = t
        return s
