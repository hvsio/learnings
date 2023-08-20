#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'angryProfessor' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY a
#

def angryProfessor(k: int, a: list[int]) -> str:
    on_timers = [x for x in a if x <= 0]
    return 'NO' if len(on_timers) >= k else 'YES'

if __name__ == '__main__':
    t = int(input().strip())
    res = []

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        res.append(angryProfessor(k, a))

    print(*res, sep='\n')
