def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

def mod_inverse(a, m):
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise Exception(f"The multiplicative inverse does not exist for {a} in Z{m}")
    else:
        return x % m

def calculate_inverse_for_domain(Z_domain):
    inverses = {}
    for num in Z_domain:
        try:
            inverse = mod_inverse(num, len(Z_domain))
            inverses[num] = inverse
        except Exception as e:
            print(e)
            inverses[num] = None
    return inverses

Z_domain = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
inverse_results = calculate_inverse_for_domain(Z_domain)
print("Multiplicative inverses in Z domain:", inverse_results)
