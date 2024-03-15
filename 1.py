import numpy as np
import time
from random import randint


# Поэлементное перемножение стандартных списков Python
res1 = []
arr1_1 = list(randint(-10000, 10000) for i in range(1000000))
arr1_2 = list(randint(-10000, 10000) for j in range(1000000))
t_start1 = time.perf_counter()
for j in range(len(arr1_1)):
    res1.append(arr1_1[j]*arr1_2[j])
all_time1 = time.perf_counter() - t_start1

# Поэлементное перемножение массивов NumPy
arr2_1 = np.array(list(randint(-10000, 10000) for i in range(1000000)))
arr2_2 = np.array(list(randint(-10000, 10000) for i in range(1000000)))
t_start2 = time.perf_counter()
res2 = np.multiply(arr2_1, arr2_2)
all_time2 = time.perf_counter() - t_start2

print(all_time1, all_time2, '\nПоэлементное перемножение массивов NumPy быстрее поэлементного перемножения стандартных списков Python в ', all_time1/all_time2, 'раз.')
