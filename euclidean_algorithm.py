# def euclidean_algorithm(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# # Euclidean Algorithm (GCD)
# gcd_result = euclidean_algorithm(25, 60)

a = 25 
b = 60
while b:
    a = b 
    b = a % b
    print("a = ",a)
    print("b = ", b)
print(a)
