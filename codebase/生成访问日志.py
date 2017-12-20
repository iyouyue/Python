def log(func):
    def inner(*args,**kwargs):
        print('you use fun %sing'%func.__name__)
        ret = func(*args,**kwargs)
        return  ret
    return inner
@log
def f1():
    print('fi')
@log
def f2():
    print('f2')
f1()
f2()