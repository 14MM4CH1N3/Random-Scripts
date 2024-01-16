def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def generators(min_a, n):
    z = {x for x in range(n) if gcd(x, n) == 1}
    for a in range(min_a, n):
        if {pow(a, p) % n for p in range(1, len(z) + 1)} == z:
            yield a

if __name__ == '__main__':
    print(next(generators(1009, 4969)))
