import random


def gcd(a, b):
    gcd_val = 0
    for i in range(1, min(a, b) + 1):
        if (a % i == 0) and (b % i == 0):
            gcd_val = i
    return gcd_val


def primitive_root(prime):
    num = 0
    primitive_root_list = []
    for i in range(1, prime):
        tmp_root_list = []
        num = num + 1
        for power in range(1, prime):
            mod = (num ** power) % prime
            tmp_root_list.append(mod)
            unique_primitive_roots = set(tmp_root_list)
            if len(unique_primitive_roots) == (prime - 1):
                primitive_root_list.append(num)

    print("Primitive Roots: ", primitive_root_list)
    index = random.randrange(0, len(primitive_root_list) - 1)
    alpha = primitive_root_list[index]
    return alpha


# returns the group members of multiplicative group (Zp)*
def group_members(n):
    lst = []
    for i in range(1, n):
        # adding all relative relative primes to list
        if gcd(i, n) == 1:
            lst.append(i)
    print("Members in group (Zp)* :", lst)
    # Euler's toutient function value
    print("Phi(p):", len(lst))
    index = random.randrange(0, len(lst))
    d_val = lst[index]
    if d_val > (p - 2):
        index = random.randint(0, len(lst) - 2)
        d_val = lst[index]

    return d_val


# p -> 2048 bit prime number
p = int(input("Enter a number (Large prime number): "))
# Choosing private key (decryption key) --> 1 <= d <= p-2
d = group_members(p)

# e1 -> encryption key (must be a primitive root of mod p)
e1 = primitive_root(p)
# e2 -> encryption key
e2 = (e1 ** d) % p
print("---------------------------------------------------------------------------")
print(f"Public Key (e1, e2, p): ({e1}, {e2}, {p})")
print("Private Key (d):", d)
print("---------------------------------------------------------------------------")

# Encryption
# M -> message such that 0 <= M <= p-1
M = int(input("Enter the message (in numerals 0-9): "))
r = group_members(p)

# Computing first part of ciphertext
C1 = (e1 ** r) % p
# Computing second part of ciphertext
C2 = ((e2 ** r) * M) % p
print("Encrypted Message (C1):", C1)
print("Encrypted Message (C2):", C2)
print("---------------------------------------------------------------------------")

# Decryption
P = (C2 * (C1 ** (p-1-d))) % p
print("Decrypted Message:", P)
print("---------------------------------------------------------------------------")
