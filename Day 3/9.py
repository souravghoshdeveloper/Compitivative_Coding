def printme(*names):
    print("typeof pass argument is",type(names))
    print("printing the passed arguments...")
    for name in names:
        print(name)
printme("jone","david","nick","smith")