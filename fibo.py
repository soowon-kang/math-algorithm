# -*- coding: utf-8 -*-

"""
Generate Fibonacci's number
"""

import math

lst = [0, 1]


def nth_fibo(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fibo_seq(n):
    global lst
    while len(lst) < n:
        lst.append(lst[-1] + lst[-2])
    return lst[n-1]


print('This program generates Fibonacci sequence.')
while True:
    try:
        m = int(input('How many numbers do you want to make? '))
        break
    except ValueError:
        print('Wrong input occurs. Please input a natural number')

print('Here are Fibonacci sequence.')
for t in fibo_seq(m):
    print(t)

n = 100
fib = nth_fibo(n)
print(n, math.log(fib, 2))
