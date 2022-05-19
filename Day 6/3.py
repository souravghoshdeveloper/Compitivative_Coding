# 2.CALCULATE THE OUTPUT USING map() function
# #out: ['DATA', 'data', 4]
# ['SCIENCE', 'science', 7]
# ['ACADEMY', 'academy', 7]
# ['OFFERS', 'offers', 6]
# ['THE', 'the', 3]
# ['BEST', 'best', 4]
# ['DATA', 'data', 4]
# ['ANALYSIS', 'analysis', 8]
# ['COURSES', 'courses', 7]
# ['IN', 'in', 2]
# ['BRAZIL', 'brazil', 6]

words = 'Data Science Academy offers the best data analysis courses in Brazil'.split()
results = map(lambda w: [w.upper(), w.lower(), len(w)], words)
for i in results:
    print(i)

