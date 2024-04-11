# RuntimeWarning: overflow encountered in exp

import numpy as np

num = 800

num = np.float128(num)

# 👇️ 2.7263745721125665673e+347
print(np.exp(num))