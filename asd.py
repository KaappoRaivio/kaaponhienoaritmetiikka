class KaaponHienoAritmetiikka(object):
    def __init__(self, x):
        self.value = x

    def lisääyksi(self):
        return KaaponHienoAritmetiikka(self.value + 1)

    def vähennäyksi(self):
        string = str(self.value)
        if string[len(string) - 1]

        __taulukko = {
            '1': '0',
            '2': '1',
            '3': '2',
            '4': '3',
            '5': '4',
            '6': '5',
            '7': '6',
            '8': '7',
            '9': '8'
        }
        return KaaponHienoAritmetiikka(self.value - 1)

    def __add__(self, other):
        print(type(other))
        if other.value == 0:
            return self
        else:
            return KaaponHienoAritmetiikka.__add__(self.lisääyksi(), other.vähennäyksi())

    def __sub__(self, other):
        print(self, other)
        return self + other * KaaponHienoAritmetiikka(-1)

    def __mul__(self, other):
        if self.value == 0:
            return KaaponHienoAritmetiikka(0)
        if self.value == 1:
            return other
        return other + KaaponHienoAritmetiikka.__mul__(KaaponHienoAritmetiikka(self.vähennäyksi()), other)

    def __str__(self):
        return str(self.value)

a = KaaponHienoAritmetiikka(int(input()))
b = KaaponHienoAritmetiikka(int(input()))
print(a, b, a.value, b.value)
print(a * b)
