# -*- coding: utf-8 -*-
"""
3n+1 problem
Receive one non-negative integer number, which is starting number,
 and then print procedure of calculation of 3n+1 problem.
If n is an odd number, n becomes 3n+1.
If n is an even number, n becomes n/2.
When the n becomes 1, the whole procedure will be finished.
"""

n = int(input('n? '))
while n > 1:
    print(n, end=' ')
    if n % 2 == 0:
        n = int(n / 2)
    else:
        n = 3*n+1
print(n)
