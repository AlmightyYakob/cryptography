from crypto.utils.pulverizer import pulverizer
from crypto.a2.constants import PUBKEY_FILE, CIPHER_FILE, PHI_FILE, ASCII_BIT_LENGTH


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

    decoded = [""] * len(binary_lines)
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
