from utils import pulverizer
from constants import A, B, MOD
from typing import Tuple


def add_points(p1: Tuple, p2: Tuple, q: int = MOD, a: int = A, b: int = B):
    x1, y1 = p1
    x2, y2 = p2

    if x1 != x2:
        # Case 1
        if x2 - x1 > q:
            _, inv_x2_x1, _ = pulverizer(x2 - x1, q)
        else:
            _, _, inv_x2_x1 = pulverizer(q, x2 - x1)

        m = (y2 - y1) * inv_x2_x1 % q
        c = y1 - m * x1 % q

        x3 = (pow(m, 2) - (x1 + x2)) % q
        y3 = (m * x3 + c) % q

        return (x3, q - y3)
    elif x1 == x2 and y1 != y2:
        # Case 2

        return (None, None)
    elif p1 == p2:
        # Case 3
        if 2 * y1 > q:
            _, inv_2y1, _ = pulverizer(2 * y1, q)
        else:
            _, _, inv_2y1 = pulverizer(q, 2 * y1)

        m = (3 * pow(x1, 2) + a) * inv_2y1 % q

        x3 = (pow(m, 2) - 2 * x1) % q
        y3 = (y1 + m * (x3 - x1)) % q

        return (x3, q - y3)
    else:
        # ????
        print("Nah fam")


def subtract_points(p1: Tuple, p2: Tuple, q: int = MOD, a: int = A, b: int = B):
    x = p2[0]
    y = -1 * p2[1]

    return add_points(p1, (x, y), q, a, b)


def multiply_point(p1: Tuple, n: int, q: int = MOD, a: int = A, b: int = B):
    x, y = p1
    for _ in range(n - 1):
        x, y = add_points(p1, (x, y), q, a, b)
        x = x % q
        y = y % q

    return (x, y)


# def good_multiply_point(p1: Tuple, n: int, q: int, a: int, b: int):
#     consts = (q, a, b)

#     if n == 0:
#         return (0, 0)
#     elif n % 2 == 0:
#         return
#             good_multiply_point(good_multiply_point(p1, n / 2, *consts), 2, *consts)
#     else:
#         return add_points(p1, good_multiply_point(p1, n - 1, *consts), *consts)
