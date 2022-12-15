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
    index = random.randrange(0, len(primitive_root_list))
    alpha = primitive_root_list[index]
    return alpha


def check_key(k1, k2):
    if k1 == k2:
        print("Shared Key is Valid:", k1)
    else:
        print("Invalid Key")


q = int(input("Enter Value of q: "))
# a -> alpha (primitive root of q)
a = primitive_root(q)
print("alpha:", a)
print("--------------------------------------------------")

# Xa and Xb are fixed by user. random value can be replaced with some chosen value
Xa = random.randrange(2, q - 1)
print("Xa:", Xa)
Xb = random.randrange(2, q - 1)
print("Xb:", Xb)
print("--------------------------------------------------")

# Computing Public Keys
Ya = (a ** Xa) % q
print("Ya:", Ya)
Yb = (a ** Xb) % q
print("Yb:", Yb)
print("--------------------------------------------------")

# Computing Session Keys
Kab = (Ya ** Xb) % q
print("Kab:", Kab)
Kba = (Yb ** Xa) % q
print("Kba:", Kba)
print("--------------------------------------------------")

# checking if key is valid or not
check_key(Kab, Kba)
print("--------------------------------------------------")
