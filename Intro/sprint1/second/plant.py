import collections
import string
from random import choice
import math

Docs = collections.namedtuple('Shoes', ['family', 'height']) #immutable, printed as a class
# namedtuple to build classes of objects that are just bundles of attributes with no custom methods, like a database record.
print(Docs)

class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self): #If you only implement one of these special methods in Python, choose __repr__ over __str__
        return f'Vector({self.x},{self.y})'
    
    def __str__(self): #this takes precedence when printing
        return 'Just a vector'
    
    def __abs__(self):
        return math.sqrt(self.x**2+self.y**2)
    
    def __add__(self, vec):
        return Vector(self.x + vec.x, self.y + vec.y)
    
    def __mul__(self, multiplier):
        return Vector(self.x*multiplier, self.y*multiplier)
    
    def __rmul__(self, multiplier):
        return self*multiplier
    
    def __bool__(self): #If __bool__ is not implemented, Python tries to invoke x.__len__(), and if that returns zero, bool returns False.
        return bool(abs(self))
        #return bool(self.x or self.y) is faster

class ShoeDocumentation:
    height = [i for i in range(1,10)]
    family = list(string.ascii_lowercase)
    suit_values = dict(a=3, b=2, c=1, d=0)

    def __init__(self):
        self._docs = [Docs(f, h) for f in self.family for h in self.height]

    def __len__(self):
        return len(self._docs)
    
    def __getitem__(self, index):
        return self._docs[index]
    
    def assign_val(self, doc: Docs):
        val = ShoeDocumentation.family.index(doc.family)
        print(val)
        return val * len(self.suit_values) + self.suit_values.get(doc.family, -1000)
    
    def print_assigned_val(self):
        for s in sorted(self._docs, key=self.assign_val): print(s)

if __name__ == '__main__':
    shoe_doc = ShoeDocumentation()
    print(shoe_doc[1])
    print(len(shoe_doc))
    print(choice(shoe_doc))
    print(shoe_doc[450::10]) #starts and gets every 10th element from there
    print([i for i in range(0,20)][18:20]) #if the index exceeds it returns the very last one
    shoe_doc.print_assigned_val()
    v = Vector(3,4)
    print(v*3)
    print(3*v)
    print(v)
