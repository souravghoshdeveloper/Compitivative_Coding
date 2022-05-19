# 1.Create a list of 3 elements and calculate the third potency of each element using a list comprehension
list1=[1,2,3]

list3=[]
for i in list1:
    list3.append(i*i*i)
print(list3)

# map function
num=(2,3,4)
result=map(lambda x:x*x*x,num)
print(list(result))


