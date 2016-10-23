# -*- coding: utf-8 -*-

"""
print the procedure of the moves of Hanoi tower problem
"""


def hanoi(src, dst, tmp, num):
    if num > 0:
        hanoi(src, tmp, dst, num-1)
        print("DISC [ %s ] moves %s -> %s" % (str(num), src, dst))
        hanoi(tmp, dst, src, num-1)


tower_src = input("Input name of departure tower: ")
tower_dst = input("Input name of destination tower: ")
tower_tmp = input("Input name of one additional tower: ")

flag = True
while flag:
    try:
        tower_num = int(input("How many discs? "))
        flag = False
    except ValueError:
        print("Please input a integer number")

hanoi(tower_src, tower_dst, tower_tmp, tower_num)
