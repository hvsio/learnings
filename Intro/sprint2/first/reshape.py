import numpy as np

numbers = np.array(input().split(' ')).astype(np.int64)
print(np.reshape(numbers, (3,3)))