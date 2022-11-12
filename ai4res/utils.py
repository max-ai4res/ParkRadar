import time

class ProgressBar:
    def __init__(self, start=0, end=100, pos=0, prefix='', suffix='', length=50, filler='█'):
        self.start = start
        self.end = end
        self.pos = pos
        self.prefix = prefix
        self.suffix = suffix
        self.length = length
        self.filler = filler
        self.start_time = None
        
    def value(self, pos, prefix='', suffix=''):
        if self.start_time is None: self.start_time = time.time_ns()
        self.pos = pos
        if prefix != '': self.prefix = prefix
        if suffix != '': self.suffix = suffix
        self.print()

    def step(self, inc=1, prefix='', suffix=''):
        self.value(self.pos + inc, prefix, suffix)
                
    def completed(self, prefix='', suffix=''):
        self.value(self.end, prefix, suffix)
        print()
        
    def print(self):
        elapsed = (time.time_ns() - self.start_time)/1e9 if self.start_time is not None else 0
        percent = (self.pos-self.start)/float(self.end-self.start)
        percent_str = "{0:.1f}".format(percent * 100)
        filled = int(self.length * percent)
        bar = self.filler * filled + '-' * (self.length - filled)
        eta = elapsed / percent * (1-percent) if percent > 0 else float('inf')
        eta_str = "{0:.2f}".format(eta)
        print(f'\r{self.prefix} |{bar}| {percent_str}% {self.suffix} [ETA: {eta_str}]', end='')