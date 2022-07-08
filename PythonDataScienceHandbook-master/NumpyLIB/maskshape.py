import math
import numpy as np

def is_prime(n):
    assert n > 1, 'Input must be larger than 1'
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


arr = np.array(range(2, 100))
non_prime_mask = [not is_prime(n) for n in arr]
prime_arr = np.ma.MaskedArray(data=arr, mask=non_prime_mask)
print(prime_arr)
# [2 3 -- 5 -- 7 -- -- -- 11 -- 13 -- -- -- 17 -- 19 -- -- -- 23 -- -- -- --
#  -- 29 -- 31 -- -- -- -- -- 37 -- -- -- 41 -- 43 -- -- -- 47 -- -- -- --
#  -- 53 -- -- -- -- -- 59 -- 61 -- -- -- -- -- 67 -- -- -- 71 -- 73 -- --
#  -- -- -- 79 -- -- -- 83 -- -- -- -- -- 89 -- -- -- -- -- -- -- 97 -- --]

arr = np.array(range(11))
print(arr.sum())  # 55

arr[-1] = -999  # indicates missing value
masked_arr = np.ma.masked_values(arr, -999)
print(masked_arr.sum())  # 45
