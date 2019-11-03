from random import randint

from utils import pulverizer


def is_prime(n, rounds=100):
    """Determine if a number is prime using Miller-Rabin."""
    # represent n = (2^r)*d + 1
    if n == 3 or n == 2:
        return True
    if n < 2:
        raise Exception("Number too low")

    d = n - 1
    r = 0

    while d % 2 == 0:
        d >>= 1
        r += 1

    if r == 0:
        # n is even
        return False

    def subtest(x):
        for _ in range(r - 1):
            x = pow(x, 2, n)

            if x == n - 1:
                return True

        return False

    for _ in range(rounds):
        a = randint(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        if not subtest(x):
            return False

    return True


def choose_e_d(phi):
    while True:
        e = randint(3, phi - 1)
        gcd, x, d = pulverizer(phi, e)

        if gcd == 1:
            return e % phi, d % phi


def compute_n_phi(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    return n, phi


def generate_p_q(k=1024):
    top = int("1" * k, 2)
    bottom = int("1" + "0" * (k - 1), 2)

    # Not sure which of these is faster/better

    # p, q = randint(bottom, top) | 1, randint(bottom, top) | 1
    # p_done, q_done = False, False
    # while not p_done or not q_done or p == q:
    #     if not p_done:
    #         p = randint(bottom, top) | 1
    #         if is_prime(p) and p != q:
    #             p_done = True

    #     if not q_done:
    #         q = randint(bottom, top) | 1
    #         if is_prime(q) and p != q:
    #             q_done = True

    #     # print(p2, q)
    # return p, q

    p, q = None, None
    while p is None or q is None or p == q:
        if p is None:
            p = randint(bottom, top) | 1
            if not is_prime(p, rounds=50) or p == q:
                p = None

        if q is None:
            q = randint(bottom, top) | 1
            if not is_prime(q, rounds=50) or p == q:
                q = None

    return p, q


def generate_keys(k):
    p, q = generate_p_q()
    n, phi = compute_n_phi(p, q)
    e, d = choose_e_d(phi)

    keys = (p, q, n, phi, e, d)
    with open("keys.txt", "w") as out:
        out.write("\n".join([str(x) for x in keys]))


def read_keys():
    with open("keys.txt", "r") as inFile:
        keys = inFile.readlines()

    keys = [int(x) for x in keys]
    return keys


def encrypt_message(msg, keys=None):
    _, _, n, _, e, _ = keys or read_keys()

    num = int.from_bytes(msg.encode(), byteorder="big")
    return pow(num, e, n)


def decrypt_message(cipher, keys=None):
    # Semi-working
    _, _, n, _, _, d = keys or read_keys()

    x = pow(cipher, d, n)
    length = int(len(bin(x))/8)
    print(x.to_bytes())
    msg = str(x.to_bytes(length, byteorder="big"), encoding="utf-8")
    return msg


def encrypt_file(path):
    # Not working
    with open(path, "r") as inFile:
        filestring = inFile.read()

    return encrypt_message(filestring)


def decrypt_file():
    pass
