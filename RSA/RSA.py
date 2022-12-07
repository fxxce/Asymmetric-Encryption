def gcd(a, b):
    gcd_val = 0
    for i in range(1, min(a, b) + 1):
        if (a % i == 0) and (b % i == 0):
            gcd_val = i
    return gcd_val


# Encryption Exponent
def e_value(fin):
    e_val = 0
    # 1 < e < ϕ(n) (fin)
    for i in range(2, fin):
        if gcd(i, fin) == 1:
            e_val = i
            break
    return e_val


# Decryption Exponent
def d_value(phi_n_val, e_val):
    d_val = 0
    for i in range(1, 10000):
        d_val = int((1 + i * phi_n_val) / e_val)
        # d = e^-1 mod ϕ(n) or we can define it as ed = 1 mod ϕ(n)
        if 1 < d_val < phi_n_val and (e_val * d_val) % phi_n_val == 1:
            break
        else:
            pass
    return d_val


p = int(input("Enter Value of p (Large Prime Number):  "))
q = int(input("Enter Value of q (Large Prime Number):  "))
m = int(input("Enter Message:  "))
print("----------------------------------------------")

n = p * q
# totient function ϕ(n)
phi_n = (p - 1) * (q - 1)
print(f"n: {n} \t ϕ(n): {phi_n}")

print("----------------------------------------------")
# e = a number less than n, such that n is relatively prime to (p - 1) x (q -1)
e = e_value(phi_n)
print(f"Private Key: ({e},{n})")

d = d_value(phi_n, e)
print(f"Public Key: ({d},{n})")
print("----------------------------------------------")

# Encryption: C = m^e mod n
C = (m ** e) % n

# Decryption: M = C^d mod n
M = (C ** d) % n

print("Encrypted Text:", C)
print("Decrypted Text:", M)
print("----------------------------------------------")
