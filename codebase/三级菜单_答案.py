"""
menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'sogo':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '汇德商厦老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{
             '朝阳大妈':{}
        },
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{
        '高丽':{}
    },
}
"""
flag = False   #定义退出标示
while not flag:   #循环执行
    for key in menu:   #遍历出菜单中一层菜单
        print(key)   #输出
    choice = input('请选择输入1:(q退出)').strip()   #选择输入
    if choice == 'q':   #选择q
        flag = True   #退出标示为真，退出循环
    if choice in menu:   #所选在菜单中
        while not flag:   #没有退出标示，继续循环
            for key2 in menu[choice]:   #遍历二层菜单
                print(key2)   #输出二层菜单中内容
            choice2 = input('请选择输入2:(q退出b返回)').strip()   #二层菜单选择输入
            if choice2 == 'q':   #选择q
                flag = True   #退出标示为真，退出循环
            if choice2 == 'b':break   #选择b，结束本次循环，继续上次循环
            if choice2 in menu[choice]:   #所选在二层菜单中
                while not flag:   #没有退出标示，继续循环
                    for key3 in menu[choice][choice2]:   #遍历三层菜单
                        print(key3)   #输出三层菜单中内容
                    choice3 = input('请选择输入3:(q退出b返回)').strip()   #三层菜单选择输入
                    if choice3 == 'q':   #选择q
                        flag = True   #退出标示为真，退出循环
                    if choice3 == 'b':break   #选择b，结束本次循环，继续上次循环
                    if choice3 in menu[choice][choice2]:   #所选在三层菜单中
                        while not flag:   #没有退出标示，继续循环
                            for key4 in menu[choice][choice2][choice3]:   #遍历四层菜单
                                print(key4)   #输出四层菜单中内容
                            choice4 = input('请选择输入4:(q退出b返回)').strip()   #四层菜单选择输入
                            if choice4 == 'b':break   #选择b，结束本次循环，继续上次循环
                            if choice4 == 'q':   #选择q
                                flag = True   #退出标示为真，退出循环
#            高级进阶版
# last = [menu]   #上一层，起始层为当前菜单，将其作为列表存储起来
# current = menu   #当前层，起始层为当前菜单
# while True:   #循环执行
#     for key in current:   #遍历菜单，是否在当前层
#         print(key)   #展示菜单
#     choice = input('请输入：').strip()   #输入选择内容
#     if choice in current:    #开始选择，如果在当前层
#         last.append(current)   #将当前层的所有选择追加进上一层列表
#         current = current[choice]   #新当前层为旧当前层所选择的下一层，然后接着循环
#     if choice == 'b':   #如果选择b
#         # if last:    #数据越界进行选择，选择只在上一层列表中查找数据
#             current = last[-1]   #当前层就是上一层最后一次存储的内容，将其取出并展示出来
#             last.pop()     #将上一层最后取出的数据删除
#     if choice == 'q':    #选择q
#         break    #退出整个循环
