# -*- coding: utf-8 -*-
def extended_euclidean_algorithm(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_euclidean_algorithm(b, a % b)
        return gcd, y, x - (a // b) * y

#changes
# Example usage:
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Extended Euclidean Algorithm
gcd_result, x, y = extended_euclidean_algorithm(num1, num2)
print(f"Extended GCD of {num1} and {num2} is: {gcd_result}")
print(f"Coefficients (x, y) are: ({x}, {y})")
