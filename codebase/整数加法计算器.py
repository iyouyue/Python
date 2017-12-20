# 实现一个整数加法计算器：
# 如：content = input(‘请输入内容:’)
# 如用户输入：5+9或5+ 9或5 + 9，然后进行分割再进行计算。
content = input('请输入内容:')
index = content.find("+")
num1 = int(content[:index])
num2 = int(content[index+1:])
print(num1 + num2)