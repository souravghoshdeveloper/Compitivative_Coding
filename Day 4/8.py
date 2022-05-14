# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

list1 = ['abc', 'xyz', 'aba', '1221']

"""
list2 = []

for i in list1:
    if len(i) >= 2 and i[0] == i[-1]:
        list2.append(i)

print(len(list2))
"""

#-------------------------------------------------
print(len([x for x in list1 if (len(x) >= 2 and x[-1] == x[0])]))