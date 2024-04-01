#inner function
def äußere_Funktion():
    def innere_Funktion():
        print("Voll in die Futterluke")
    innere_Funktion()

äußere_Funktion()

#decorator
import functools

def wer_hat_das_gras_weggeraucht(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("NI")
        x = func()
        print("ER")
        return  x       #!!!
    return wrapper()

@wer_hat_das_gras_weggeraucht
def gg():
    print("GG")

#namespace
x="g"
def e():
    x="e"
    def l():
        x="l"       #L E G B
        print(x)
    l()
e()

#iterator
# sequence_iter.py

class SequenceIterator:
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._sequence):
            item = self._sequence[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration

for item in SequenceIterator([1, 2, 3, 4]):
    print(item)


