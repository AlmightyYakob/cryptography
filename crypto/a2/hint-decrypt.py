import math

PUBKEY_FILE = "a2-hint.pubkeys"
CIPHER_FILE = "a2-hint.cipher"

ASCII_ZERO = 48
ASCII_NINE = 57


def main():
    with open(PUBKEY_FILE, "r") as inFile:
        key_length, N, e = [int(line.strip()) for line in inFile.readlines()]

    with open(CIPHER_FILE, "r") as inFile:
        cipher_lines = [int(line.strip()) for line in inFile.readlines()]

    mapping = {}
    decoded = []

    for line in cipher_lines:
        if line in mapping:
            decoded.append(mapping[line])
        else:
            for i in range(ASCII_ZERO, ASCII_NINE + 1):
                num = pow(i, e, N)

                if num == line:
                    mapping[line] = i
                    decoded.append(i)
                    break

    phi = int("".join([str(x - ASCII_ZERO) for x in decoded]))
    if math.gcd(phi, e) == 1:
        with open("a2.phi", "w") as outFile:
            outFile.write(str(phi))
    else:
        print("Error: gcd(phi, e) != 1 !!!")


if __name__ == "__main__":
    main()
