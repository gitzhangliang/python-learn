print('默认参数--------------------------------')
#默认参数 定义默认参数要牢记一点：默认参数必须指向不变对象！
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(5))
print(power(5,3))

print('可变参数--------------------------------')
#可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
nums = [1, 2, 3]
print(calc(*nums))

print('关键字参数--------------------------------')
#关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('Adam', 45, gender='M', job='Engineer')
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

print('命名关键字参数--------------------------------')
#命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)
person('Jack', 24, city='Beijing', job='Engineer')

def person1(name, age, *args, city, job='python'):
    print(name, age, args, city, job)
person1('z',1,'2',3,city='xian',job='java')
person1('z',1,'2',3,city='xian')

#对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的
#*args是可变参数，args接收的是一个tuple；

#**kw是关键字参数，kw接收的是一个dict。
#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数