import time


def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print('Execution time: {}'.format(time.time() - t))
        return res

    return tmp


@timer
def coun(i):
    while i != 1000000:
        i += 1

coun(1)


def cache(func):
    values = {}

    def wrapper(*args):
        if args not in values:
            values[args] = func(*args)
        return values[args]

    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))


def profiled(func):
    def inner(*args, **kwargs):
        inner.calls += 1
        return func(*args, **kwargs)
    inner.calls = 0
    return inner


@profiled
def coun(i):
    while i != 1000000:
        i += 1

coun(10)
print(coun.calls)

coun(20)
print(coun.calls)


def once(func):
    def inner(*args, **kwargs):
        if not inner.called:
            print('really doing init')
            func(*args, **kwargs)
            inner.called = True
        else:
            print('not first init')
    inner.called = False
    return inner


@once
def coun():
    print('Calling decorated function')


coun()
coun()
coun()
coun()
