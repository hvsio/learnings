import random
import bisect
import array

def arr():
    a = array.array('i', [1,2,1,1]) #need to define the data type while declaring an array, since an array stores only similar values.
    print(a)
    a[2] = 3
    a[1] = 'a'
    print(a)

def memory_view():
    arr = array.array('B',[1,2,3,4,5,6])
    m1 = memoryview(arr)
    print(m1)
    m2 = m1.cast('B', shape=[2,3])
    m2[1,0] = 41
    print(m2.tolist())
    print(id(m1), id(m2), id(arr))
    print(arr)

def evaluate(exp, env) -> any:
    match exp:
        case ['define', *_]:
            return 
        case ['quote', _]:
            return exp
        case ['if', test, cons, alt]:
            if evaluate(test, env):
                return evaluate(consequence, env)
            else:
                return evaluate(alternative, env)
        case ['lambda', [*params], *body]: #In a sequence pattern, * can appear only once per sequence. 
            #Here we have two sequences: the outer and the inner.
            return lambda x: body * x
        case ['define', [str() as name, *params], value_exp]:
            env[name] = evaluate(value_exp, env)
        case _:
            raise BaseException('Match exception')
        
def slicing_in_reverse():
    print("define"[::3])
    print("define"[::-2])
    #to evaluate the expression seq[start:stop:step],
    #Python calls seq.__getitem__(slice(start, stop, step))
    a = [x for x in range(10)]
    print(a[slice(1,9,3)])

def ellipsis(arr): #it can be passed as an argument to functions and as part of a slice specification
    return arr[3: ...] #that works only for numpy, multidimensional arrays/tenosrs


class GenExp:
    def __init__(self, source_list, func):
        self.source_list = source_list
        self.func = func

    def generate(self):
        return (self.func(x) for x in self.source_list)
    

'''
    When you see a tuple in code, you know its length will never change.
    A tuple uses less memory than a list of the same length, and it allows Python to do some optimizations.
    References in a tuple cannot be deleted or replaced.
    Object is only hashable if its value cannot ever change

    [record] = query_returning_single_row() - only one result holding it
'''
if __name__ == '__main__':
    ge = GenExp([14, 34, 56, 55], lambda x: x % 5)
    example = ge.generate()
    t = tuple(example) + ('abc',)
    print(t, example)
    *a, b = t
    print(a,b)
    a, b = b, a 
    print(a,b)
    slicing_in_reverse()
    #print(ellipsis([[i].extend([i*j for j in range(10, 15, 2)]) for i in range(10)]))

    for x in ((random.randint(1, 100), random.randbytes(5)) for _ in range(9)):
        print("%d/%s" % x)

    l = [list() for x in range(3)]
    l[0].append(1)

    l_faulty = [[]] * 3
    l_faulty[0].append(1)
    print(l_faulty)
    print(l_faulty[0] == l_faulty[1])
    print(id(l_faulty))
    a = [1,2,3,4,5]
    shallow_copy = a[1:4]
    shallow_copy[2] = 5
    print(id(a), id(shallow_copy))
    memory_view()
