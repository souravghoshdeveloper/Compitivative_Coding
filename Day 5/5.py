list=[[2,3,4],[1,4,16,64],[3,6,9,12]]
sortlist=lambda x:(sorted(i) for i in x)
second_largest =lambda x, f :[y[len(y)-2] for y in f(x)]
res = second_largest(list,sortlist)
print(res)