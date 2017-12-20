def login(home):
    """
    在这里从新定义一个高阶函数，
    这就是decorator。
    我们一会儿会仔细分析。
    """
    def wrapper(*args, **kwargs):
        user = "youyue"   # 假设这是数据库中的用户名和密码
        passwd = "123"
        username = input("输入用户名：")
        password = input("输入密码：")
        if username == user and password == passwd:
            return home(*args, **kwargs)
        else:
            print("用户名或密码错误。")
    return wrapper


@login     # 利用python的@语法，把decorator置于home函数的定义处 相当于home = login(home)
def home():
    print("欢迎来到YueNet首页！")

home()

# 运行看看，是不是没改变home源码和home的调用方式，给home添加了登录验证的功能？
#
# 其实，这里@login相当于做一这么一件事：home = login(home)
#
# 那么当执行23行时就是这样的：login(home)()
#
# 　　login(home)是什么？他就是调用login这个函数后的返回值，即wrapper
#
#       此时，login(home)()即变成了 wrapper()
#
# 　　执行wrapper() ,返回home()函数并执行home()
#
# 整个过程就是这样。
