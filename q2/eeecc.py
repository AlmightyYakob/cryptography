from utils import pulverizer, print_pulverizer
from constants import A, B, MOD
from typing import Tuple


def add_points(
    p1: Tuple, p2: Tuple, q: int = MOD, a: int = A, b: int = B, print_out=False
):
    x1, y1 = p1
    x2, y2 = p2

    pulverizer_func = print_pulverizer if print_out else pulverizer

    if x1 != x2:
        # Case 1
        if print_out:
            print(f"m = ({y2} - {y1})/({x2} - {x1}) % {q}")
            print(f"INVERSE OF ({x2} - {x1} = {(x2 - x1) % q} (mod {q})):")
        _, _, inv_x2_x1 = pulverizer_func(q, (x2 - x1) % q)

        m = (y2 - y1) * inv_x2_x1 % q
        c = y1 - m * x1 % q

        x3 = (pow(m, 2) - (x1 + x2)) % q
        y3 = (m * x3 + c) % q

        if print_out:
            print(f"m = {m}")
            print(f"c = ({y1} - {m}*{x1}) % {q} = {c}")
            print(f"x3 = ({m}^2 - {x1} + {x2}) % {q} = {x3}")
            print(f"y3 = ({m}*{x3} + {c}) % {q} = {y3}")
            print(f"Reflection y3 = q -  y3 = {q - y3}")
            print(f"New Point: {(x3, q - y3)}")
            print("")

        return (x3, q - y3)
    elif x1 == x2 and y1 != y2:
        # Case 2
        return (None, None)
    elif p1 == p2:
        # Case 3
        if print_out:
            print(f"m = (3 * {x1}^2 + {a})/(2*{y1}) % {q}")
            print(f"INVERSE OF (2*{y1} = {2*y1 % q} (mod {q})):")
        _, _, inv_2y1 = pulverizer_func(q, (2 * y1) % q)

        m = (3 * pow(x1, 2) + a) * inv_2y1 % q

        x3 = (pow(m, 2) - 2 * x1) % q
        y3 = (y1 + m * (x3 - x1)) % q

        if print_out:
            print(f"m = {m}")
            print(f"x3 = ({m}^2 - 2*{x1}) % {q} = {x3}")
            print(f"y3 = ({y1} + {m}*({x3} - {x1})) % {q} = {y3}")
            print(f"Reflection y3 = {q} - {y3} = {q - y3}")
            print(f"New Point: {(x3, q - y3)}")
            print("")

        return (x3, q - y3)
    else:
        # ????
        print("Nah fam")


def subtract_points(
    p1: Tuple, p2: Tuple, q: int = MOD, a: int = A, b: int = B, print_out=False
):
    x = p2[0]
    y = -1 * p2[1]

    return add_points(p1, (x, y), q, a, b, print_out=print_out)


def multiply_point(
    p1: Tuple,
    n: int,
    q: int = MOD,
    a: int = A,
    b: int = B,
    print_out=False,
    print_tables=False,
):
    x, y = p1
    for i in range(n - 1):
        x, y = add_points(p1, (x, y), q, a, b, print_out=print_tables)

        if x is None and y is None:
            if print_out:
                print("POINT AT INFINITY")
            break

        if print_out:
            print(f"POINT*{i+2} = {(x, y)}")

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
