# Write a Python program to add two given lists and find the difference between lists. Use map() function.
list1 = []
for i in range(4):
    input1 = int(input("Enter the value to list 1 "))
    list1.append(input1)

list2 =[]
for j in range(4):
    input2 = int(input("Enter the value to list 2 "))
    list2.append(input2)

result = map(lambda x,y: x + y, list1,list2)
print(list(result))

result1 = map(lambda x,y: x - y, list1,list2)
print(list(result1))