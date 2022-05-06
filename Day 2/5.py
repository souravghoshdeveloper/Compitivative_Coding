"""
those four lines
x=[]
for i in range (6):
x.append ( i**2 )
print(x)

by using comprehension logic we convert the four line to two lines of ABOVE prgm
"""
t=[i**2 for i in range(6)]
print(t)