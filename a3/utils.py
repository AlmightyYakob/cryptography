from constants import A, B, G, P, Q


def pulverizer(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0


def elgamel_decrypt(cipher, mask, p=P, a=A):
    alpha_a = pow(mask, a, p)
    _, _, inv_alpha_a = pulverizer(p, alpha_a)
    msg = (cipher * inv_alpha_a) % p

    return msg
