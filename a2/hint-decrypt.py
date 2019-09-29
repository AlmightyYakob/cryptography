from textwrap import wrap
import rsa

PUBKEY_FILE = "a2-hint.pubkeys"
CIPHER_FILE = "a2-hint.cipher"

ASCII_BIT_LENGTH = 8


def main():
    with open(PUBKEY_FILE, "r") as inFile:
        pubkey_lines = [int(line.strip()) for line in inFile.readlines()]

    with open(CIPHER_FILE, "r") as inFile:
        cipher_lines = [int(line.strip()) for line in inFile.readlines()]

    key_length, N, e = pubkey_lines

    for i, line in enumerate(cipher_lines):
        print(f"{'-'*10}{i}{'-'*10}")
        print(rsa.decrypt(line, N))
        exit()
        bin_message = bin(pow(line, e, N))[2:]
        chunked_bin_message = wrap(bin_message, ASCII_BIT_LENGTH)
        print(chr(int(chunked_bin_message[0], 2)))
        message = "".join([int(x, 2) for x in chunked_bin_message])
        print(message)


if __name__ == "__main__":
    main()
