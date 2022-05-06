# Data Structure
# Q1. Write a program to find out highest 3 value from list
no_of_data_you_want_to_add = int(input("no of data you want to add? "))
list1 = []
i = 0
while(i < no_of_data_you_want_to_add):
    user_input = int(input("Enter a value? "))
    list1.append(user_input)
    i =i +1

print(list1)

list1.sort()

print(list1[-3:])


# Q2. Write a program to remove the duplicate no from list
list2 = []
for a in list1:
    if a not in list2:
        list2.append(a)
print(list2)