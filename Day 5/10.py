print((lambda x, y, z=3: x + y + z)(1, y=2))

print((lambda *args : sum(args)/len(args))(1,2,3))