from constants import A, B, MOD
from typing import Tuple


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
