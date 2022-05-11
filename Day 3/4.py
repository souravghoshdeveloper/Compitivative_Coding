def table(n):
    return lambda a:a*n;
n=int(input("Enter the number?"))
b=table(n)
for i in range (1,11):
    print(n,"X",i,"m",b(i));
