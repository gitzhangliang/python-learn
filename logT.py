import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now():
    print('2015-3-25')

print(now())#now = log(now)=wrapper(没有 @functools.wraps(func)情况下)
print(now.__name__)#so name is wrapper