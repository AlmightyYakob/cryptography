from crypto.utils.pulverizer import pulverizer


def elgamel_decrypt(cipher, mask, p, a):
    alpha_a = pow(mask, a, p)
    _, _, inv_alpha_a = pulverizer(p, alpha_a)
    msg = (cipher * inv_alpha_a) % p

    return msg
