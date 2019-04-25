#Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算
from collections import Iterable
print(isinstance('as',Iterable))

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
s=[1,2,3]
it = iter(s);
print(isinstance(it,Iterable))
print(next(it))