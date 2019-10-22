from random import randint


def is_prime(n, rounds=100):
    """Determine if a number is prime using Miller-Rabin."""
    # represent n = (2^r)*d + 1
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

    for _ in range(n):
        a = randint(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        if not subtest(x):
            return False

    return True


def choose_e_d():
    pass


def compute_n_phi():
    pass


def generate_p_q(k=4096):
    pass


def generate_keys():
    # Generate_p_q
    # Compute N and phi
    # Choose e and d
    pass


def encrypt_file():
    pass


def decrypt_file():
    pass
