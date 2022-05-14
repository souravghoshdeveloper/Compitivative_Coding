# Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
# Sample Output:
# Double the number of 15 = 30
# Triple the number of 15 = 45
# Quadruple the number of 15 = 60
# Quintuple the number 15 = 75
def func(n):
    return lambda x : x * n

result = func(2)
print("Double the number of 15 =", result(15))

result = func(3)
print("Triple the number of 15 =", result(15))

result = func(4)
print("Quadruple the number of 15 =", result(15))

result = func(5)
print("Quintuple the number 15 =", result(15))
