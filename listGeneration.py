import os
print([x*x for x in range(10)])
print([x*x for x in range(10) if x%2 == 0])
print([x*x for x in range(10) if (x*x*x)%3 == 0])
print([x*x for x in range(10) if (x+1)%3 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])

print([d for d in os.listdir('.')])

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])