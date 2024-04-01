class SquareIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            square = self.data[self.index] ** 2
            self.index += 1
            return square
        else:
            raise StopIteration

# Verwendung:
iterator = SquareIterator([1, 2, 3, 4, 5])
for square in iterator:
    print(square)
