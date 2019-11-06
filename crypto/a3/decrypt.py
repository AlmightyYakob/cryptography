from crypto.utils.elgamel import elgamel_decrypt
from constants import A, B, G, P, Q


with open("a3.cipher") as cipherFile:
    point_pairs = cipherFile.readlines()
    point_pairs = [line.split(",") for line in point_pairs]

    point_pairs = [(int(x), int(y)) for (x, y) in point_pairs]


message = []
for mask, cipher in point_pairs:
    message.append(elgamel_decrypt(cipher, mask, p=P, a=A))
    # print(message[-1])

# Dunno what to do with them at this point
message = "".join([str(chr(x)) for x in message])
print(message)
