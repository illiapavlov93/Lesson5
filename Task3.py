import time


def lru(f):
    lru.fuse = 0
    lru.cache = {}
    lru.cachuse = 0
    lru.time = 0
    lru.cachesize = 128

    def wrapper(a):
        if lru.time == 0:
            lru.time = time.time()
        if a in lru.cache.keys():
            print('cache use', lru.cache[a])
            lru.cachuse += 1
        else:
            r = f(a)
            print('function use', r)
            lru.cache[a] = r
            lru.fuse += 1
        if len(lru.cache) + 1 > lru.cachesize:
            lru.cache.popitem()

    def cache_info():
        print('Function use', lru.fuse)
        print('Cache use', lru.cachuse)
        print('Cache space', int(lru.cachesize - lru.cachuse))
        if lru.time == 0:
            print('Cache time 0')
        else:
            print('Cache time', lru.time - int(time.time()))

    wrapper.cache_info = cache_info

    def cache_clear():
        lru.cache.clear()
        lru.fuse = 0
        lru.cachuse = 0
        lru.time = 0
        print('Cache clear')

    wrapper.cache_clear = cache_clear
    return wrapper


@lru
def double(a):
    return a + a


double(10)
double(10)
double(20)
double(20)
double.cache_info()
double.cache_clear()
double.cache_info()
