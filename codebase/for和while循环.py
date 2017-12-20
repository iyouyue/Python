# 1.使用while循环输出1 2 3 4 5 6     8 9 10
# count = 0
# while count < 10:
#     count += 1
#     if count ==7:
#         print('')
#         continue
#     else:
#         print(count)
#-----------------------
# 2.编写（for循环）和（while循环），利用索引遍历出每一个字符
# msg='hello longlong 666'
# msg = msg.replace(" ", '')
# for i in msg:
#     print(i)
#----------------------
# msg = 'hello world'
# count = 0
# while True:
#     if count < len(msg):
#         print(msg[count])
#         count += 1
#     else:break
#--------------------
# 9.编写while循环，让用户输入用户名和密码，如果用户名为空或者数字，则重新输入
#--------------
name = "alex"
password = "123"
flag = True
while flag:
    username = input("请输入用户名:")
    if username == "" or username.isdigit():
        continue
    else:pwd = input("请输入密码:")
    if username == "alex" and password == "123":
            flag = False
            print("您登陆成功")
    else:
         print("您的用户名或密码有误，请重新输入")
         continue
