import sys

sys.path.append("..")  # Adds higher directory to python modules path.

from q2.eeecc import decrypt_message


with open("a4.allkeys") as allkeys:
    p, A, B, G, P, N = allkeys.readlines()
    p, A, B, N = int(p), int(A), int(B), int(N)
    G, P = tuple(G.split(" ")), tuple(P.split(" "))
    # print(p, A, B, G, P, N)
    # print(type(p), type(A), type(B), type(G), type(P), type(N))

with open("a4.cipher") as cipherFile:
    point_pairs = cipherFile.readlines()
    point_pairs = [line.split(" ") for line in point_pairs]

    point_pairs = [((int(a), int(b)), (int(c), int(d))) for (a, b, c, d) in point_pairs]


message = []
for cipher, mask in point_pairs:
    message.append(decrypt_message(cipher, mask, N, p))
    print(message[-1])

message = int("".join([str(x) for (x, _) in message]))
print(message)
