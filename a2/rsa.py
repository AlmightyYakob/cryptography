from random import randint


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


def choose_e_d():
    pass


def compute_n_phi(p, q):
    n = p*q
    phi = (p - 1) * (q - 1)
    return n, phi


def generate_p_q(k=4096):
    top = int("1" * k, 2)
    bottom = int("1" + "0" * (k - 1), 2)

    p = randint(bottom, top) | 1
    q = randint(bottom, top) | 1
    while p == q:
        p = randint(bottom, top) | 1
        q = randint(bottom, top) | 1

    p_valid, q_valid = False, False
    while not p_valid or not q_valid or p == q:
        if not p_valid:
            if is_prime(p) and p != q:
                p_valid = True
            else:
                # p += 2
                p = randint(bottom, top) | 1

        if not q_valid:
            if is_prime(q) and p != q:
                q_valid = True
            else:
                # q += 2
                q = randint(bottom, top) | 1

        print(p_valid, q_valid)
    return p, q


def generate_keys():
    # Generate_p_q
    # Compute N and phi
    # Choose e and d
    pass


def encrypt_file():
    pass


def decrypt_file():
    pass
