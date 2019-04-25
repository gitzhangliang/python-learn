g = (x * x for x in range(10))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
for v in g:
    print("next:",v)

def fib(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
f = fib(3);
print(f)
for v in f:
    print(v)