PUBKEY_FILE = "a2.pubkeys"


def main():
    with open(PUBKEY_FILE, "r") as inFile:
        pubkey_lines = [int(line.strip()) for line in inFile.readlines()]

    print(pubkey_lines)


if __name__ == "__main__":
    main()
