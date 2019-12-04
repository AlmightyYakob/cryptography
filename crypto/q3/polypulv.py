import numpy as np


def poly_pulverizer(a: np.ndarray, b: np.ndarray):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""

    a = np.array(a)
    b = np.array(b)
    if a.size < b.size:
        a, b = b, a

    a = np.trim_zeros(a, trim="f") % 2
    b = np.trim_zeros(b, trim="f") % 2

    r = np.ndarray((1,))
    x1, x2, y1, y2 = 1, 0, 0, 1
    while np.trim_zeros(r).size != 0:
        q, r = np.polydiv(a, b)

        a = b
        b = r
        x2 = np.polysub(x1, np.polymul(q, x2))
        y2 = np.polysub(y1, np.polymul(q, y2))
        x1, y1 = x2, y2

        a = np.trim_zeros(a % 2, trim="f")
        b = np.trim_zeros(b % 2, trim="f")
    return b, x2, y2


if __name__ == "__main__":
    a = [1, 0, 0, 0, 1, 1, 0, 1, 1]
    b = [0, 0, 0, 1, 0, 0, 0, 1, 0]

    print(poly_pulverizer(a, b))
