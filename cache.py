from collections import OrderedDict

cache_size = 10
cache = OrderedDict ()
def retrieve (key):
    if key in cache:
        return Image.open (key)
    else:
        cache[key] = Image.open (key)
        if (len (cache) > cache_size):
            cache.popitem (False) #FIFO
        return cache[key]
