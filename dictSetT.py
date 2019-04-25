d = {'name':'zhangliang','age':1}
print(d)
d['sex'] = 'man'
print(d)
print(d.get('age'))
print(d.get('like'))
print(d.get('like','python'))
d.pop('age')
print(d)

for key in d:
    print(key)
for value in d.values():
    print(value)
for k, v in d.items():
    print(k+':'+v)


s = set([1, 2, 3])
print(s)