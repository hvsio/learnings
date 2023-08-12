import random
import numpy as np
import logging
import importlib

logger = logging.getLogger(__name__)
class MyCustomError(ValueError):
    '''heheheh'''

class BasicArtithmetics:
    def __init__(self, name):
        print('Created!')
        self.name = name
        print(self.name)

    @property #getter, cannot exist without a setter
    def heheheh(self):
        return self.name
        
    @heheheh.setter
    def heheheh(self, name):
        self.name = name

    @classmethod
    def division_rounddown(calling_class, x,y):
        print(calling_class)
        return x // y
    
    @staticmethod
    def exponential(x,y):
        return x**y
    
    def comparison_operator(x: int, y: bool):
        return x == y
    
    def get_bool_val(x):
        return bool(x)
    
    def get_tested():
        a = [1,2,3,4]
        b = [1,2,3,4]
        print("Objects are equal, the same ", a == b)
        print("But they do not refer to the same object in the memory ", a is b)


    def analyze_list():
        '''
            lists are mutable data types as their entries can be replaced, modified, order changed.
            They are also dynamic as we can add and remove entries on demand.
        '''
        li = list(np.random.randint(1, 10, size=10))
        print(li)
        print("Reversed: ", li[::-1])
        print("Every third entry: ", li[::3])
        li_copy = li[:]
        print(li_copy == li, li_copy is li)
        li.insert(len(li), random.randint(0,100))

    def analyze_tuple(self):
        '''
            In tuples elements are immutable and can be accessed faster. It has no build in methods tho.
            Faster iterations.
        '''
        tup = tuple([1,2,3,4,5,6,7,8,9, [10]])
        a, *b, c = tup
        print(a,b, c, " Unpacks to a list if more than one entry")
        tup[len(tup)-1].append(10)
        print(a)
        print(tup)
        print(hash(tup))

    def accessing_dict():
        dict = {'a': 1, 'b': 2, 'c': None}
        print(dict.get('a'))
        print(dict.get('d'), 5)
        print(dict['b'])
        print(dict['d'])

    def set_creation():
        set = {1,2,3,4,5,6,7}
        set.add(5)
        set.add(10)
        set_1 = {11, 'aaa'}
        print(set & set_1)
        print(set | set_1)
        print(set ^ set_1, " Symmetric diff - unique elements")
        print(set >= set_1, " Is it a superset of the smaller one?")

    def loop():
        for x in range(10):
            print(x)
            if (x == 9):
                try:
                    raise MyCustomError("Random Error")
                except (Exception, KeyError) as e:
                    '''
                    When inside an except clause, you might want to, 
                    for example, log that a specific type of error happened, and then re-raise. 
                    The best way to do this while preserving the stack trace is to use a bare raise statement.
                    Raising a new error causes a loss of stack.
                    '''
                    logger.error(e)
                    raise #this prints the stack trace on top of the customly printed error
                finally:
                    print('Freeing resources')

    def iterables():
        iterable = iter(['1',2,4,5,6])
        try:
            print(iterable[1])
        except TypeError as e:
            print("Trying to get indexed entry from iterable", e)

        try:
            sorted(iterable)
        except Exception as a:
            print(e)

        try:
            for x in range(10):
                print(next(iterable))
        except StopIteration as e:
            print(e)

    def func(**kwargs):
        print(kwargs['example'])
    
    def func1(*args):
        print(args[1])

    def anonymous():
        return (lambda x: x**2)(5)
    
class Advanced(BasicArtithmetics): #if the class was above the parent class the parent would be undefined
    def __init__(self, not_name, age):
        self.not_name = not_name
        super().__init__('why not')
        print(self.not_name, age)

    @property
    def age(self):
        return self.age
    
    @age.setter
    def age(self, ageee):
        self.age = ageee

    def advanced_method():
        print(np.random.rand(3,4))

class Almost():
    def __init__(self, adoration=False):
        self.adoration = adoration

class Abstract(Almost, Advanced):
    def __init__(self, *args, **kwargs):
        Almost.__init__(self, adoration=args[0])
        Advanced.__init__(self, kwargs['hehe'], age=2)

    def idk(self):
        print("Idk")

class Generators():
    def __init__(self, x, y):
        print('creating', x, y)
        self.x = x

    @property
    def y():
        return self.y
    
    @y.setter
    def setter(self, y):
        print('setter')
        self.y = y

    @classmethod
    def generator_comprehension(cls, x):
        vals = (x**x for x in [1,2,3,4,5])
        for x in vals:
            print(x)

    @classmethod
    def create(cls, **attr):
        print(attr)
        return cls(attr['x'], attr.get('y', 4))
    
    @staticmethod
    def yeilding(x: int):
        for i in range(x):
            print(i)
            if (i == 9):
                yield 'u won'


if __name__ == '__main__':
    inp = input("Put your preference:\n")
    print(inp)
    adv = Advanced('Random name', 55)
    ba = BasicArtithmetics('Alicja')
    print(type(adv), type(ba), adv == ba)
    print(isinstance(adv, Advanced), isinstance(adv, BasicArtithmetics)) ## both true
    print(Advanced.exponential(3,4))
    print(adv.exponential(3,4))
    abstract = Abstract('one', 'two', 'three', hehe=123)
    generator = Generators(3,4)
    generator.generator_comprehension(generator.x)
    new_gen = generator.create(x=3, y=4)
    new_gen.yeilding(20)
    print(next(new_gen.yeilding(20)))
    ba.analyze_tuple()