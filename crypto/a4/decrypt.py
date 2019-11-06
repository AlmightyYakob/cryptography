
from crypto.utils.eeecc import decrypt_message


with open("a4.allkeys") as allkeys:
    p, A, B, G, P, N = allkeys.readlines()
    p, A, B, N = int(p), int(A), int(B), int(N)
    G, P = tuple(G.split(" ")), tuple(P.split(" "))

with open("a4.cipher") as cipherFile:
    point_pairs = cipherFile.readlines()
    point_pairs = [line.split(" ") for line in point_pairs]

    point_pairs = [((int(a), int(b)), (int(c), int(d))) for (a, b, c, d) in point_pairs]


message = []
for cipher, mask in point_pairs:
    message.append(decrypt_message(cipher, mask, n=N, q=p, a=A, b=B))
    print(message[-1])

chars = [chr(x) for x, _ in message]
string = "".join([str(c) for c in chars])
print(string)
