def f(x):
    return  x*x
r = map(f,[1,2,3])
print(next(r))
print(list(r))


t = map(f,(1,2,3))
print(next(t))
print(list(t))

print(list((1,2)))


print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))