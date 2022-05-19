# Create two functions, one to elevate a number to square and the second to elevate to cube. Run both functions to the elements at the same time.
listOfNumbers = [0, 1, 2, 3, 4]
def cube(n):
    return (n**2)
def square(n):
    return (n**3)
funcs = [cube, square]
for i in listOfNumbers:
    results = map(lambda x: x(i), funcs)
    print(list(results))
