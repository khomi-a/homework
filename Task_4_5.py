from time import perf_counter
from time import sleep
import numpy as np

def timit(func, n=1):
    def wrapper(a, b):
        t1 = []
        t2 = []
        for i in range(n):
            tic = perf_counter()
            func(a, b)
            tac = perf_counter()
            t1.append(tic)
            t2.append(tac)
        t1, t2 = np.array(t1), np.array(t2)
        t = t2 - t1
        print('time:', round(np.mean(t), 4), 's +-', round(np.std(t), 4), 's')
        return func(a, b)
    return wrapper

def slow_add(a: int, b: int) -> int:
    sleep(1)
    return a+b

slow_add_dec = timit(slow_add, 4)
print(slow_add_dec(1, 2))
