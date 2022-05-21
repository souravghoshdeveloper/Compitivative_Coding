from functools import reduce
def both_true(a, b):
    return bool(a and b)
print(reduce(both_true, [1, 1, 1, 1, 1]))
print(reduce(both_true, [1, 1, 1, 1, 0]))
print(reduce(both_true, [], True))


from functools import reduce

# creating a function to check if both arguments are True or not
def is_true(a, b):
   return bool(a or b)

print(reduce(is_true, [1, 1, 0, 1, 1]))

print(reduce(is_true, [0, 0, 0, 0, 0]))