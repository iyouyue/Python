name = input("请输入你的名字：")
age = int(input("请输入你的年龄："))
job = input("请输入你的工作：")
hobbie = input("请输入你的爱好：")

msg = """
---------------- info of %s --------------------
Name : %s
Age  : %d
job  : %s
Hobbie: %s
------------------ end -------------------------
""" %(name,name,age,job,hobbie)
print(msg)