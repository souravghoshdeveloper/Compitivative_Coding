# f= lambda a:a*a
# lambda a, b: a+b
# (lambda x: x+1)(2)
# programe to filter out only the even items from a list ,((((( lamba alawys return object , reduce alaways return list))))

my_list = [1,5,4,6,8,11,3,12]
new_list=list(filter(lambda x: (x%2==0),my_list))
print(new_list)
# map function
my_list = [1,5,4,6,8,11,3,12]
new_list=list(map(lambda x:(x%2==0),my_list)) # map is a iterable elements
print(new_list)
# casting
string1="Sourav Ghosh love sayani mondal"
print(lambda string1:string1)
(lambda string1: print(string1))(string1)

