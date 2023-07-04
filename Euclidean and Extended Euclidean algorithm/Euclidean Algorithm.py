# Euclidean algorithm for calculating GCD of two numbers
num1 = int(input("Enter first number to find its GCD: "))
num2 = int(input("Enter second number to find its GCD: "))

r1 = num1
r2 = num2

while (r2 > 0):
    rem = r1 % r2
    print(f"1st Num: {r1} \t 2nd Num: {r2} \t Remainder: {rem}")
    r1 = r2
    r2 = rem
    if (r2 == 0):
        print("Since remainder = 0, the value of 2nd Num will be the GCD")

print(f"The GCD of {(num1, num2)} is: {r1}")
