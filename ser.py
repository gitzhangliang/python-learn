import pickle
d = dict(name='Bob', age=20, score=88)
f = open('g:\\1.txt', 'wb')
pickle.dump(d, f)
f.close()