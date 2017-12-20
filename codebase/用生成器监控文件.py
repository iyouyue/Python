#生成器函数
def tail():
    f = open('xxx','r',encoding = 'utf-8')
    f.seek(0,2)
    while True:
        line = f.readline()
        if line:
            yield line

g = tail()
for i in g:
    print(i.strip())