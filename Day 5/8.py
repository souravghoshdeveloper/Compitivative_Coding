from functools import reduce

lis=[1,3,5,6,2,]
print("the maximum element of the list is:",end="")
print(reduce(lambda a,b : a if a>b else b,lis))