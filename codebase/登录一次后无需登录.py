#用装饰器实现，访问art或者dar函数，登陆一次之后，无需再次登录
flag = False
def login(func):
    def inner(*args,**kwargs):
        global flag
        if flag == False:
            username = input('用户名:')
            password = input('密码:')
            if username == 'alex' and password == 'somebody':
                print('登录成功')
                flag = True
        if flag == True:
            ret = func(*args,**kwargs)
            return ret
    return inner

@login
def art():
    print('欢迎来到文章页')
art()

@login
def dar():
    print('欢迎来到日记页')
dar()