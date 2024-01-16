def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def totient_function(grr):
    count = 0
    for i in range(1, grr):
        if gcd(i, grr) == 1:
            count += 1
    return count

def prime_factors(num):
    factors = []
    divisor = 2
    while divisor * divisor <= num:
        while (num % divisor) == 0:
            factors.append(divisor)
            num //= divisor
        divisor += 1
    if num > 1:
        factors.append(num)
    return factors

def is_primitive_root(a, b, factors):
    if a == 0 or a == 1:
        return False
    if pow(a, totient_function(b), b) != 1:
        return False
    for factor in factors:
        if pow(a, totient_function(b) // factor, b) == 1:
            return False
    return True

def find_primitive_roots(c):
    factors = prime_factors(totient_function(c))
    primitive_roots = []
    for a in range(2, c):
        if is_primitive_root(a, c, factors):
            primitive_roots.append(a)
    return primitive_roots

def compute_orders_and_roots(d):
    print(f"For n = {d}:")
    primitive_roots = find_primitive_roots(d)
    for a in range(1, d):
        order = totient_function(d)
        if gcd(a, d) == 1:
            for k in range(1, order):
                if pow(a, k, d) == 1:
                    order = k
                    break
            print(f"Order of {a} mod {d}: {order}")
        else:
            print(f"GCD of {a} and {d}: {gcd(a, d)}")
    print(f"Primitive Roots: {primitive_roots}\n")
    print(len(primitive_roots))

def calculate_mod_table(e, a_limit, b_limit):
    print(f"Table of a^b mod {e} for 1 <= a <= {a_limit} and 0 <= b <= {b_limit}:\n")
    header = ["a/b"] + [str(b) for b in range(b_limit + 1)]
    print("\t".join(header))
    for a in range(1, a_limit + 1):
        row_values = [str(a)]
        for b in range(b_limit + 1):
            result = pow(a, b, e)
            row_values.append(str(result))
        print("\t".join(row_values))

if __name__ == "__main__":
    n = 31
    compute_orders_and_roots(n)
    #calculate_mod_table(n, n - 1, n - 1)