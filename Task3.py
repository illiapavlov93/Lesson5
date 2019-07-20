from collections import OrderedDict
import time


def lru_size(cachesize):
    lru_size.fuse = 0
    lru_size.cache = OrderedDict()
    lru_size.cachuse = 0
    lru_size.time = time.time()
    lru_size.cachesize = cachesize

    def lru(f):
        def wrapper(a):
            if len(lru_size.cache) + 1 > cachesize:
                print('deleting from cache :{}'.format(lru_size.cache.popitem(False)))
            if a not in lru_size.cache:
                lru_size.fuse += 1
                r = f(a)
                lru_size.cache[a] = r
                print('Func use: {}, Cache: {}\n'.format(r, dict(lru_size.cache)))
            else:
                lru_size.cachuse += 1
                print('Cache use: {}, Cache: {}\n'.format(lru_size.cache[a], dict(lru_size.cache)))
            return lru_size.cache.get(a)

        def cache_info():
            print('Function use: {}'.format(lru_size.fuse))
            print('Cache use: {}'.format(lru_size.cachuse))
            print('Cache space: {}'.format(int(lru_size.cachesize - len(dict(lru_size.cache)))))
            if lru_size.time == 0:
                print('Cache time: 0\n')
            else:
                print('Cache time: {}\n'.format(lru_size.time - int(time.time())))

        wrapper.cache_info = cache_info

        def cache_clear():
            lru_size.cache.clear()
            lru_size.fuse = 0
            lru_size.cachuse = 0
            lru_size.time = 0
            print('Cache clear\n')

        wrapper.cache_clear = cache_clear

        return wrapper
    return lru


@lru_size(3)
def double(a):
    return a + a


double(10)
double(10)
double(20)
double.cache_info()
double(20)
double(30)
double(40)
double.cache_info()
double.cache_clear()
double.cache_info()
double(10)
double.cache_info()
