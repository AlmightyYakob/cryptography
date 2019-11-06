with open("a3.pubkeys") as pubkeys:
    P, Q, G, B = [int(x) for x in pubkeys.readlines()]

with open("a.txt") as a_constant:
    A = int(a_constant.readline())
