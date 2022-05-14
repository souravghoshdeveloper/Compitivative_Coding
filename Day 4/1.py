# Write a Python program to triple all numbers of a given list of integers. Use Python map.

list1 = [20, 58, 106, 98]

"""
print(list1[0] * 3)
print(list1[1] * 3)
print(list1[2] * 3)
print(list1[3] * 3)"""

#------------------------
"""for i in list1:
    print(i *3)"""

#-------------------------
def triple(n):
    return n*3
num=[20,96,82,58]
result =map(triple,num)
print(list(result))