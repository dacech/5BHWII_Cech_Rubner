class SimpleCounter:
    def __init__(self, stop):
        self.stop = stop
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.stop:
            self.count += 1
            return self.count
        else:
            raise StopIteration

# Verwendung:
counter = SimpleCounter(5)
for number in counter:
    print(number)
