import random
# print(random.randint(100000,999999))
# print(random.randrange(100000,1000000))  #弊端：不能以0开头，数字不能重复
#===============================
# l = []
# for i in range(6):
#     rand = random.randint(0,9)
#     l.append(str(rand))
# print('-'.join(l))
#--------------包含字母 版本------------------
l = []
for i in range(6):
    alpha = chr(random.randint(65,90))
    alpha_low = chr(random.randint(97,122))
    num = str(random.randint(0,9))
    ret = random.choice([alpha,num,alpha_low])
    l.append(ret)
print(''.join(l))

