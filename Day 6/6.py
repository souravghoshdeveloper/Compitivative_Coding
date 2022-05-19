#
range(-5, 5)
list(filter((lambda x: x < 0), range(-5,5)))

a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
print (list(filter(lambda x: x in a, b)))