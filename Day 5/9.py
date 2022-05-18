high_ord_func = lambda x, func: x + func(x)

print(high_ord_func(2, lambda x: x * x))
print(high_ord_func(2, lambda x: x + 3))
