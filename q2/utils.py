from .constants import A, B, MOD
from typing import Tuple


def fix_arg(x, i, length):
    return f"{' '*(length - len(str(x)))}{str(x)}"


def print_table_header(row_length):
    row_names = ["A", "B", "Q", "R", "X1", "Y1", "X2", "Y2"]
    header = [fix_arg(x, i, row_length) for i, x in enumerate(row_names)]
    print(f"|{'|'.join(header)}|")


def print_table_row(a, b, q, r, x1, y1, x2, y2, row_length):
    args = [a, b, q, r, x1, y1, x2, y2]
    fixed_args = [fix_arg(x, i, row_length) for i, x in enumerate(args)]
    print(f"|{'|'.join(fixed_args)}|")


def print_pulverizer(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    rows = []

    # x0, x1, y0, y1 = 0, 1, 1, 0
    x1, y1, x2, y2 = 1, 0, 0, 1
    q, r = None, None
    while r != 0:
        q = a // b
        r = a % b

        rows.append((a, b, q, r, x1, y1, x2, y2))

        a, b = b, r
        y1, y2 = y2, y1 - q * y2
        x1, x2 = x2, x1 - q * x2

    row_length = 0
    for row in rows:
        row_length = max(row_length, max([len(str(x)) for x in row]))

    print_table_header(row_length)
    for row in rows:
        print_table_row(*row, row_length)
    print("")

    _, _, _, _, _, _, x2, y2 = rows[-1]

    return b, x2, y2


def pulverizer(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0


def on_curve(p1: Tuple):
    x, y = p1

    left_side = pow(y, 2, MOD)
    right_side = (pow(x, 3) + A * x + B) % MOD

    if left_side == right_side:
        return True
    else:
        return False
