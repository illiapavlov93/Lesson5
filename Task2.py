import functools


def my_decorator(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        print('Calling decorated function')
        return f(*args, **kwargs)

    return wrapper


@my_decorator
def example():
    """Called example function"""


example()

print(example.__name__, example.__doc__)


@functools.singledispatch
def add(a, b):
    print(a + b)


@add.register(int)
def _(a, b):
    print("argument is of type ", type(a))
    print(a + b)


@add.register(str)
def _(a, b):
    print("argument is of type ", type(a))
    print(a + b)


@add.register(list)
def _(a, b):
    print("argument is of type ", type(a))
    print(a + b)


add(1, 2)
add('Python', 'Programming')
add([1, 2, 3], [5, 6, 7])
