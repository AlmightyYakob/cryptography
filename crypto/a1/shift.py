import sys


KEY = 3
ASCII_BOTTOM = 65
CHAR_SPACE = 26
ENCRYPT_ARG = "-e"
DECRYPT_ARG = "-d"


def encrypt(msg):
    msg = "".join(filter(lambda c: c.isalpha(), msg))
    newMsg = "".join(
        map(
            lambda x: chr(((ord(x) + KEY - ASCII_BOTTOM) % CHAR_SPACE) + ASCII_BOTTOM),
            msg.upper(),
        )
    )
    return newMsg


def decrypt(msg):
    newMsg = "".join(
        map(
            lambda x: chr(((ord(x) - KEY - ASCII_BOTTOM) % CHAR_SPACE) + ASCII_BOTTOM),
            msg.upper(),
        )
    )
    return newMsg


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if DECRYPT_ARG in sys.argv:
            index = sys.argv.index(DECRYPT_ARG)
            filename = sys.argv[index+1]
            with open(filename, "r") as file:
                print(decrypt(file.read()))

        if ENCRYPT_ARG in sys.argv:
            index = sys.argv.index(ENCRYPT_ARG)
            filename = sys.argv[index+1]
            with open(filename, "r") as file:
                print(encrypt(file.read()))
