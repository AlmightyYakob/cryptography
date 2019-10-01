PUBKEY_FILE = "a2.pubkeys"
CIPHER_FILE = "a2.cipher"
PHI_FILE = "a2.phi"

ASCII_BIT_LENGTH = 8


def read_pubkey():
    with open(PUBKEY_FILE, "r") as inFile:
        key_length, N, e = [int(line.strip()) for line in inFile.readlines()]

    return (N, e)


def read_cipher():
    with open(CIPHER_FILE, "r") as inFile:
        cipher_lines = [int(line.strip()) for line in inFile.readlines()]

    return cipher_lines


def read_phi():
    with open(PHI_FILE, "r") as phi_file:
        return int(phi_file.read().strip())


def pulverizer(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0


def main():
    cipher_lines = read_cipher()
    N, e = read_pubkey()
    phi = read_phi()

    g, x, d = pulverizer(phi, e)

    while d < 0:
        d += phi

    # print(g, x, d)

    binary_lines = []
    for i, line in enumerate(cipher_lines):
        binary_lines.append(bin(pow(line, d, N))[2:])

    decoded = [""]*len(binary_lines)
    for i, x in enumerate(binary_lines):
        len_mod = len(x) % ASCII_BIT_LENGTH
        x = ("0" * (ASCII_BIT_LENGTH - len_mod)) + binary_lines[i]

        for j in range(0, len(x), ASCII_BIT_LENGTH):
            a = x[j : j + ASCII_BIT_LENGTH]
            decoded[i] += chr(int(a, 2))

    for line in decoded:
        line = line[::-1].replace("\\n", "\n")
        print(line)
        print("")


if __name__ == "__main__":
    main()
