def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)
base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))
r = power(base, exponent)
print("Result:", r)