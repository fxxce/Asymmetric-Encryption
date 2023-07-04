# Extended euclidean algorithm to find the GCD of two integers & to compute the coefficient that satisfy Bézout's identity.
# Bézout's identity -> for any two ints "a" and "b" there exist integers "x" and "y" such that: ax + by = gcd(a, b)

a = int(input("Enter first integer a: "))
b = int(input("Enter second integer b: "))

# Remainders
r1 = a
r2 = b

# Coefficients of a
s1 = 1
s2 = 0

# Coefficients of b
t1 = 0
t2 = 1

while (r2 > 0):
    quot = r1 // r2
    rem = r1 % r2
    r1 = r2
    r2 = rem
    s = s1 - (quot * s2)
    s1 = s2
    s2 = s
    t = t1 - (quot * t2)
    t1 = t2
    t2 = t

print(f"(s1, t1): ({s1},{t1}) --> Satisfies the Bézout's identity")
print(f"{a} * {s1} + {b} * {t1} = gcd({a}, {b})")

# checking if the obtained value satisfy ax + by = gcd(a, b)
print(f"Evaluating ax + by: {(s1 * a) + (t1 * b)}")
print(f"GCD of ({a}, {b}) : {r1}")

# calculating inverse
if (r1 == 1):
    if (t1 > 0):
        print("Modular Inverse:", t1)
    else:
        while (t1 < 0):
            t1 = t1 + a
        print("Modular Inverse:", t1)
else:
    print("Inverse Does not Exist")
