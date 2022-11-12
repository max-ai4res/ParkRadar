import time

class ProgressBar:
    def __init__(self, start=0, end=100, val=0, prefix='', suffix='', length=50, filler='█'):
        self.start = start
        self.end = end
        self.val = val
        self.prefix = prefix
        self.suffix = suffix
        self.length = length
        self.filler = filler
        self.start_time = None
        self.end_time = None
        
    def value(self, val, prefix=None, suffix=None):
        if self.start_time is None: self.start_time = time.time_ns()
        self.val = val
        self.print(prefix=prefix, suffix=suffix)

    def step(self, inc=1, prefix=None, suffix=None):
        self.value(self.val + inc, prefix, suffix)
                
    def completed(self, prefix=None, suffix=None):
        self.value(self.end, prefix, suffix)
        print()
        
    def print(self, prefix=None, suffix=None):
        if prefix is not None: self.prefix = prefix
        if suffix is not None: self.suffix = suffix

        if self.val >= self.end and self.end_time is None:
            self.end_time = time.time_ns()
            
        step_time = self.end_time if self.end_time is not None else time.time_ns()
        
        elapsed = (step_time - self.start_time)/1e9 if self.start_time is not None else 0
        percent = (self.val-self.start)/float(self.end-self.start)
        percent_str = "{0:.1f}".format(percent * 100)
        filled = int(self.length * percent)
        bar = self.filler * filled + '-' * (self.length - filled)
        if percent < 1:
            eta = elapsed / percent * (1-percent) if percent > 0 else float('inf')
            eta_str = "{0:.2f}".format(eta)
            time_str = f'[ETA: {eta_str}s]'
        else:
            elt_str = "{0:.2f}".format(elapsed)
            time_str = f'[TIME: {elt_str}]'
            
        print(f'\r{self.prefix} |{bar}| {percent_str}% {self.suffix} {time_str}', end='')