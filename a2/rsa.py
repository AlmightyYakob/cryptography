def is_prime(n, rounds=100):
    """Determine if a number is prime using Miller-Rabin."""
    # n = (2^r)d + 1
    new_n = n - 1

    while bin(new_n)[-1] != "0":
        new_n >> 1

    pass


def choose_e_d():
    pass


def compute_n_phi():
    pass


def generate_p_q():
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
