def euclidean_algorithm(a, b):
    while b:
        a, b = b, a % b
    return a


# Euclidean Algorithm (GCD)
gcd_result = euclidean_algorithm(num1, num2)
print(f"GCD of {num1} and {num2} is: {gcd_result}")

# Extended Euclidean Algorithm
gcd_result, x, y = extended_euclidean_algorithm(num1, num2)
print(f"Extended GCD of {num1} and {num2} is: {gcd_result}")
print(f"Coefficients (x, y) are: ({x}, {y})")
