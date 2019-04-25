name = ['a','b','c']
name.append('d')
print(name)
name.insert(1,'A')
print(name)
deleteName = name.pop()
print(deleteName)
print(name)

for n in name:
    print(n)

print('---------------------------------')
L =  list(range(100))
print(L)
print(L[:10])
print(L[-3:])
print(L[:10:2])
print(L[:10:1])

