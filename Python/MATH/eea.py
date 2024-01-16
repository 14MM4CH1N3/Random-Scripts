def geecd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = geecd(b % a, a)
        return gcd, y - (b // a) * x, x


def inverse(a, m):
    gcd, x, y = geecd(a, m)
    if gcd != 1:
        raise ValueError("inverse dne")
    else:
        return (x % m + m) % m


a = 13
b = 31
z = inverse(a, b)
print(f"inverse of {a} mod {b} is: {z}")