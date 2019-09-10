import numpy as np

KEY_FILE = "./key_matrix.txt"
LOWEST_CHAR_N = 65


def verify_key(key):
    det = np.linalg.det(key)
    print(det)
    recip = np.reciprocal(det)
    print(recip)


def read_key(input_file):
    with open(input_file, "r") as in_file:
        lines = in_file.readlines()

    lines = [list(map(int, line.split())) for line in lines]
    return np.array(lines)


def inverse_key(key):
    pass


def gen_key(n):
    pass


def encode(msg):
    msg = msg.upper()
    key = read_key(KEY_FILE)

    matrix = list(map(lambda x: ord(x) - LOWEST_CHAR_N, list(msg)))
    N = len(matrix) / key.shape[0]
    matrix = np.split(np.array(matrix), N)

    for i, col in enumerate(matrix):
        matrix[i] = np.matmul(key, col) % 26

    result = list(map(lambda x: chr(x + LOWEST_CHAR_N), np.concatenate(matrix)))
    result = "".join(result)
    return result


def decode(msg):
    msg = msg.upper()
    matrix = list(map(lambda x: ord(x) - LOWEST_CHAR_N, list(msg)))

    inv_key = np.linalg.inv(read_key(KEY_FILE))
    N = len(matrix) / inv_key.shape[0]
    print(inv_key)
    matrix = np.split(np.array(matrix), N)
    print("matrix", matrix)
    for i, col in enumerate(matrix):
        # matrix[i] = inv_key.dot(col) % 26
        matrix[i] = np.matmul(inv_key, col) % 26
        print("after col", matrix[i])
    result = list(map(lambda x: chr(int(x) + LOWEST_CHAR_N), np.concatenate(matrix)))
    result = "".join(result)
    print(result)


verify_key(read_key(KEY_FILE))
exit()
# encoded = encode("ATTACKATDAWN")
encoded = encode("ATTACKATDAWN")
print(encoded)
decoded = decode(encoded)
