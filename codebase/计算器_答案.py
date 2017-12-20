import re
#处理符号用的
def dealwith_symbol(express):
    if '--' in express:express = express.replace('--','+')
    if '+-' in express:express = express.replace('+-','-')
    if '-+' in express:express = express.replace('-+','-')
    if '++' in express:express = express.replace('++','+')
    return express
#处理乘除法
def mul_div(express):
    #a*b  a/b
    if '*' in express:
        a,b = express.split('*')
        ret = float(a)*float(b)
    elif '/' in express:
        a, b = express.split('/')
        ret = float(a) / float(b)
    return str(ret)

# 将没有括号的子表达式中的乘除法先提取出来，再计算加减法
def simplify_express(express_son):  #(9-2*5/3)
    while True:  #取乘除法计算
        ret = re.search(r'\d+\.?\d*[*/]-?\d+\.?\d*',express_son)   #(9-2*5/3)
        if ret:
            mul_div_express = ret.group()     #2*5
            result = mul_div(mul_div_express)   #10
            express_son = express_son.replace(mul_div_express,result,1)   #(9-3.3)
            express_son = dealwith_symbol(express_son)
        else:break
    express_son = dealwith_symbol(express_son)
    num_lst = re.findall(r'[\+\-]?\d+\.?\d*',express_son)  #(-8)
    sum = 0
    for i in num_lst:
        sum += float(i)
    return str(sum)

# 将表达式中的括号提取出来
def remove_bracket(express):
    #\([^\(\)]+\)、\([^\(]+?\)、\([\-\d\+\/\*\.]+\)
    while True:
        ret  = re.search(r'\([^\(\)]+\)',express)
        if ret:
            express_no_bracket = ret.group()  #express_no_bracket: 没有括号的表达式
            sum = simplify_express(express_no_bracket)
            express = express.replace(express_no_bracket,sum,1)
        else:break
    return simplify_express(express)

e = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
new_express = e.replace(' ','')
result = remove_bracket(new_express)
print(result)
