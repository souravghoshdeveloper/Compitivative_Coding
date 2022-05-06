"""
those four lines
x=[]
for i in range (6):
x.append(i**2)
print(x)

by using comprehension logic we convert the four line to two lines of ABOVE prgm
"""
t=[i**2 for i in range(6)]
print(t)



"""
x=[]
for i in [1,2,3]:
    for j in [3,4,5]:
        if i != j:
            x.append ((i,j))
print(x)"""

# Soluction
y=[(i,j )for i in [1,2,3] for j in [3,4,5] if i!=j ]
print(y)


# write a prgm to find out 1 to 10 from list comprehension
"""
list1 = []
for i in range(0,10):
    if (i %2 != 0):
        list1.append(i)
print(list1)"""

# Soluction
B=[i for i in range(0,10) if (i %2 != 0)]
print(B)


# write a prgm to find out factorial of file using list comprehension
