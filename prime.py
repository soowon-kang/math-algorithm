# -*- coding: utf-8 -*-

"""
Check whether input number is prime or not
Receive one non-negative integer number, which is n
"""


def is_prime(n):
    if (n < 2) or (n % 2 == 0):
        return False

    sqn = int(n ** 0.5)
    flag = False
    for i in range(3, sqn + 1, 2):
        flag |= (n % i == 0)

    return not flag


while True:
    try:
        n = int(input('n? '))
        break
    except ValueError:
        print('wrong input occurs.')

print('%d is' % n, end=' ')
if not is_prime(n):
    print('not', end=' ')
print('a prime number.')
