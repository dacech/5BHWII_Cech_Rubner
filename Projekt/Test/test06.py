
class SQR():
    def __init__(self,data):
        self.data = data
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.data):
            sqr = self.data[self.index] **2
            self.index += 1
            return sqr
        else:
            raise StopIteration

test = SQR([1,2,3,4,5])
for item in test:
    print(item)



import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        starttime = time.perf_counter()
        value = func(*args, **kwargs)
        endtime = time.perf_counter()
        runtime = endtime - starttime
        print(f"Zeit: {runtime:.4f}")
        return value
    return wrapper()

