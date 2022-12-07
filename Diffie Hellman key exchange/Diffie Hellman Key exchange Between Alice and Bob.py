import random


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
    index = random.randint(0, len(primitive_root_list))
    alpha = primitive_root_list[index]
    return alpha


prime_num = int(input("Alice and Bob Enter a Prime Number: "))
print("Alice and Bob agreed on prime number:", prime_num)
print("--------------------------------------------------")

# a -> alpha (primitive root of prime_num)
a = primitive_root(prime_num)
print("Alice and bob agreed on primitive root:", a)
print("--------------------------------------------------")

# Xa = Alice's private/secret key, Xb = Bob's private/secret key
Xa = int(input("Alice enter Secret Key: "))
Xb = int(input("Bob enter Secret Key: "))
print("--------------------------------------------------")

# Ya = Alice's public key, Yb = Bob's public key
Ya = (a ** Xa) % prime_num
print("Alice's Public Key:", Ya)
Yb = (a ** Xb) % prime_num
print("Bob's Public Key:", Yb)
print("--------------------------------------------------")

# Computing Session Keys
Kab = (Ya ** Xb) % prime_num
print("(Alice) Calculated Shared:", Kab)
Kba = (Yb ** Xa) % prime_num
print("(Bob) Calculated Shared:", Kba)
print("--------------------------------------------------")

if Kab == Kba:
    print("Shared Key:", Kab)
    print("Valid Key, Eve can't intercept the traffic.")
else:
    print("Invalid Key")
print("--------------------------------------------------")