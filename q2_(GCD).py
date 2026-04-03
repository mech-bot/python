n1 = int(input("Enter your num1: "))
n2 = int(input("Enter your num2: "))

gcd = 0
for i in range(1, min(n1, n2) + 1):
    if n1 % i == 0 and n2 % i == 0:
        gcd = i
print("The GCD of", n1, "and", n2, "is:", gcd)