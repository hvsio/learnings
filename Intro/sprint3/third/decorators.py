import time
import functools   # decorators standard library
from functools import singledispatch
from collections import abc
import fractions
import decimal
import html
import numbers

# CLASS BASED DECORATOR
DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'
class clock:
    def __init__(self, fmt=DEFAULT_FMT):
        self.fmt = fmt

    def __call__(self, func):
        def clocked(*_args):
            t0 = time.perf_counter()
            _result = func(*_args)
            elapsed = time.perf_counter() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(self.fmt.format(**locals()))
            return _result

        return clocked


def make_averager(func):
    series = []   # closure

    def averager(new_value):
        # The closure for averager extends the scope of that function to include the binding for the free variable series.
        series.append(new_value)   # series is a free variable
        total = sum(series)
        return total / len(series)

    return averager


def make_averager_optimized():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager


@make_averager
@clock
@functools.cache
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1) * factorial(n - 2)


@singledispatch   # TODO try it with interface/protocols,
def htmlize(obj: object) -> str:
    """
    ALSO does it cascade? will int or float-specific handler capture the parameter?
    ANSWER: singledispatch logic seeks the implementation with the most specific matching type, regardless of the order they appear in the code.
    """
    content = html.escape(repr(obj))
    return f'<pre>{content}</pre>'


@htmlize.register
def _(text: str) -> str:
    content = html.escape(text).replace('\n', '<br/>\n')
    return f'<p>{content}</p>'


@htmlize.register
def _(seq: abc.Sequence) -> str:
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'


@htmlize.register
def _(n: numbers.Integral) -> str:
    return f'<pre>{n} (0x{n:x})</pre>'


@htmlize.register
def _(n: bool) -> str:
    return f'<pre>{n}</pre>'


@htmlize.register(fractions.Fraction)
def _(x) -> str:
    frac = fractions.Fraction(x)
    return f'<pre>{frac.numerator}/{frac.denominator}</pre>'


@htmlize.register(decimal.Decimal)
@htmlize.register(float)
def _(x) -> str:
    frac = fractions.Fraction(x).limit_denominator()
    return f'<pre>{x} ({frac.numerator}/{frac.denominator})</pre>'


avg = make_averager_optimized()
avg(19)
avg(1)
avg(3)
print(
    avg.__code__.co_freevars,
    avg.__code__.co_varnames,
    list(avg.__closure__),
    avg.__closure__[0].cell_contents,
)
# So factorial now actually holds a reference to the clocked function.
# From now on, each time factorial(n) is called, clocked(n) gets executed
t0 = time.perf_counter()
print(factorial(6), factorial.__name__)
elapsed = time.perf_counter() - t0
print(elapsed)

registry = set()


def register(active=True):
    def decorate(func):
        print('running register' f'(active={active})->decorate({func})')
        if active:
            registry.add(func)
        else:
            registry.discard(func)

        return func

    return decorate


@register(active=False)
def f1():
    print('running f1()')


@register()
def f2():
    print('running f2()')


def f3():
    print('running f3()')
