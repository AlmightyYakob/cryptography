import binascii
import click
from random import randint

from crypto.utils.pulverizer import pulverizer


DEFAULT_K = 1024


def is_prime(n, rounds=100):
    """Determine if a number is prime using Miller-Rabin."""
    # represent n = (2^r)*d + 1
    if n < 2:
        raise Exception("Number too low")
    if n == 2 or n == 3:
        return True

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

            if x == 1:
                return False
            if x == n - 1:
                return True

        return False

    for _ in range(rounds):
        a = randint(2, n - 2)
        x = pow(a, d, n)

        if x != 1 and x != n - 1 and not subtest(x):
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
    top = pow(2, k) - 1
    bottom = pow(2, k - 1)

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

    keys = (p, q, n, e, d)
    return keys


def save_keys(keys, outfile):
    with open(outfile, "w") as out:
        out.write("\n".join([str(x) for x in keys]))


def read_keys(path):
    with open(path, "r") as inFile:
        keys = inFile.readlines()

    keys = [int(x) for x in keys]
    return keys


def encrypt_message(msg, keys):
    _, _, n, e, _ = keys

    data = binascii.hexlify(msg.encode())
    num = int(data, 16)

    if num > n:
        raise Exception("Message too large for public modulus (n)")

    return pow(num, e, n)


def decrypt_message(cipher, keys):
    _, _, n, _, d = keys

    x = pow(cipher, d, n)
    hex_x = hex(x)[2:]
    hex_x = f"0{hex_x}" if len(hex_x) == 1 else hex_x

    msg = binascii.unhexlify(hex_x).decode()
    return msg


def encrypt_file(path, keys):
    # Done character by character
    _, _, n, _, _ = keys

    encrypted_chars = []
    with open(path, "r") as inFile:
        data = inFile.read()

    for char in data:
        encrypted_chars.append(str(encrypt_message(char, keys)))

    # with open(out, "w") as outFile:
    #     outFile.write("\n".join(encrypted_chars))

    return encrypted_chars


def decrypt_file(path, keys):
    # Done character by character
    _, _, n, _, _ = keys

    decrypted = ""
    with open(path, "r") as inFile:
        lines = inFile.readlines()

    for line in lines:
        decrypted += decrypt_message(int(line), keys)

    # with open(out, "w") as outFile:
    #     outFile.write(decrypted)

    return decrypted


def out_option(func):
    func = click.option("-o", "--out", help="The file to write the result to.")(func)

    return func


@click.group()
def cli():
    pass


@cli.command("generate")
@click.option("-o", "--out", required=True, help="The file to write the result to.")
@click.option(
    "-k",
    "--key-length",
    default=DEFAULT_K,
    show_default=True,
    help="The length in bits of the primes.",
)
def generate(out, key_length):
    keys = generate_keys(key_length)
    save_keys(keys, out)


@cli.command("encrypt")
@click.argument("filename")
@out_option
@click.option(
    "-k",
    "--keys",
    "key_file",
    required=True,
    help="The file containing the keys, "
    "separated by newlines in the order p, q, n, e, d",
)
def encrypt(filename, out, key_file):
    keys = read_keys(key_file)

    char_list = encrypt_file(filename, keys=keys)
    out_string = "\n".join(char_list)

    if out:
        with open(out, "w") as outFile:
            outFile.write(out_string)
    else:
        print(out_string)


@cli.command("decrypt")
@click.argument("filename")
@out_option
@click.option(
    "-k",
    "--keys",
    "key_file",
    required=True,
    help="The file containing the keys, "
    "separated by newlines in the order p, q, n, e, d",
)
def decrypt(filename, out, key_file):
    keys = read_keys(key_file)
    decrypted_string = decrypt_file(filename, keys)

    if out:
        with open(out, "w") as outFile:
            outFile.write(decrypted_string)
    else:
        print(decrypted_string)


if __name__ == "__main__":
    cli()
