# -*- coding: utf-8 -*-

"""
Calculate a factorial number.
"""

import math


def fact_rec(m):
    if m == 0:
        return 1
    return m * fact_rec(m - 1)


def fact_iter(m):
    result = 1
    for i in range(1, m + 1):
        result *= i
    return result


n = input('n? ')
print('%d! is %d' % (n, fact_iter(n)))

print('log(%d!) = %f' % (n, math.log10(fact_iter(n))))
