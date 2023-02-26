from numba import jit,njit

import numpy as np
import time
import random



def monte_carlo_pi(nsamples):
    acc = 0
    for i in range(nsamples):
        x = random.random()
        y = random.random()
        if (x ** 2 + y ** 2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples

start_time=time.time()
p=monte_carlo_pi(10000000)
print(p)
end_time=time.time()
ztime=end_time-start_time
print(f'运行时间{ztime}')