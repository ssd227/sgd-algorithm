import time
from functools import wraps


def calc_time(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        t2 = time.time()
        print('cost_time: {}s'.format(t2 - t1))
        return res

    return decorated
