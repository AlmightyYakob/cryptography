import os

DIR_NAME = os.path.dirname(os.path.realpath(__file__))

with open(f"{DIR_NAME}/a3.pubkeys") as pubkeys:
    P, Q, G, B = [int(x) for x in pubkeys.readlines()]

with open(f"{DIR_NAME}/a.txt") as a_constant:
    A = int(a_constant.readline())
