# Write a Python program to square the elements of a list using map() function
def square(n):
    return n*n
num=[90,56,89,78]
result=list(map(square,num))
print(result)