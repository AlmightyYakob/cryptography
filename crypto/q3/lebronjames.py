import numpy as np

b1 = np.array([73, 2])
b2 = np.array([193, 1])

q = 1
while abs(q) != 0:
    if np.linalg.norm(b2) < np.linalg.norm(b1):
        b1, b2 = b2, b1

    raw_q = np.dot(b1, b2) / np.dot(b1, b1)
    q = np.round(raw_q)
    r = b2 - q * b1
    # b2 = b1
    b2 = r

print(f"b1 == {b1}")
print(f"b2 == {b2}")

b1norm = np.linalg.norm(b1)
b2norm = np.linalg.norm(b2)
smallest_norm = min(b1norm, b2norm)

smallest_vector = b1 if b1norm < b2norm else b2
print(f"Smallest vector is {smallest_vector} | Norm = {smallest_norm}")

print(f"|x| = {abs(smallest_vector[0])}")
