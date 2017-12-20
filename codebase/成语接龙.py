import random

def idiom_exists(x):
    """判断是否为成语的函数，参数为字符串，判断该字符串是否在成语库中"""
    with open('idiom.txt','r',encoding='utf-8') as f:
        for i in set(f.readlines()):
            if x == i.strip():
                return True
        return False

def idiom_test(idiom1, idiom2):
    """判断两个成语是否达成接龙条件"""
    if idiom2[0] != idiom1[-1] or len(idiom2) != 4:
        return False
    return True

def idiom_select(x):
    """核心代码部分，参数x为成语，返回该成语的接龙匹配成语"""
    if x == None:
        with open('idiom.txt','r',encoding='utf-8') as f:
            return random.choice(f.readlines())[:-1]
    else:
        with open('idiom.txt','r',encoding='utf-8')as f:
            base = f.readlines()
            random.shuffle(base)
            for i in base:
                if i[:-1] == x or len(i) != 5:
                    continue
                if i[0] == x[-1]:
                    return i[:-1]
        return None

def idiom_start(start = 0):
    """start参数表示先后手，0表示电脑先手，1表示玩家先手；返回值代表游戏结果，为0表示玩家失败，为1代表玩家胜利"""
    memory = set()  #记忆集合，用于判断成语是否被重复使用
    #如果电脑先手，电脑先抛出的第一个成语我们给点限制，要求它的接龙成语必须存在
    if start == 0:
        while True:
            t = idiom_select(None)
            if idiom_select(t) != None and len(t) == 4:
                break
        print(t)
    else:
        p = input("请输入成语:")
        if p.strip() == '':
            print("游戏结束！你输了")
            return 0
        if idiom_exists(p) == False:
            print("游戏结束！该成语不存在")
            return 0
        memory.add(p)
        cycle_flag = 0  #控制while True循环次数
        while True:
            t = idiom_select(p)
            cycle_flag += 1
            if t not in memory:
                break
            if cycle_flag == 10:
                t = None
                break
        if t == None:
            print("恭喜你，你赢了！")
            return 1
        else:
            print(t)
            memory.add(t)
    while True:
        p = input("请输入成语:")
        if p.strip() == '':
            print("游戏结束！你输了")
        if idiom_exists(p) == False:
            print("游戏结束！该成语不存在")
            return 0
        if p in memory:
            print("游戏结束！该成语已被使用过")
            return 0
        if idiom_test(t, p) == False:
            print("游戏结束！你未遵守游戏规则")
            return 0
        memory.add(p)
        cycle_flag = 0
        while True:
            t = idiom_select(p)
            cycle_flag += 1
            if t not in memory:
                break
            if cycle_flag == 10:
                t = None
                break
        if t == None:
            print("恭喜你，你赢了！")
            return 1
        else:
            print(t)
            memory.add(t)

#测试运行
idiom_start()























# import random
# def idiom_exists(x):
#     with open('idiom.txt','r',encoding='utf-8') as f:
#         for i in set(f.readlines()):
#             if x == i.strip(0):
#                 return True
#             return False
# def idiom_test(idiom1,idiom2):
#     if idiom2[0] != idiom1[-1] or len(idiom2) != 4:
#         return False
#     return True
#
# def  idiom_select(x):
#     if x == None:
#         with open('idiom.txt','r',encoding='utf-8')as f:
#             base = f.readlines()
#             random.shuffle(base)
#             for i in base:
#                 if  i[:-1] == x or len(i)!=5:
#                     continue
#                 if i[0] == x[-1]:
#                     return i[:-1]
#         return None
#
# def idiom_start(start = 0):
#     memory = set()
#     if start == 0:
#         while True:
#             t = idiom_select(None)
#             if idiom_select(t) != None and len(t) == 4:
#                 break
#         print(t)
#     else:
#         p = input('please input idiom.txt:')
#         if p.strip()== '':
#             print("game over , you lose")
#             return  0
#         if idiom_exists(p) == False:
#             print('game over,the idiom.txt 404')
#             return 0
#         memory.add(p)
#         cycle_flag = 0
#         while True:
#             t = idiom_select(p)
#             cycle_flag += 1
#             if t not in memory:
#                 break
#             if cycle_flag == 10:
#                 t = None
#                 break
#         if t == None:
#             print('you win')
#             return  1
#         else :
#             print(t)
#             memory.add(t)
#         while True:
#             p = input('please input idiom.txt:')
#             if p.strip() == '':
#                 print('game over, you lose')
#             if idiom_exists(p) == False:
#                 print('game over the idiom.txt 404')
#                 return  0
#             if p in memory:
#                 print('game over,the idiom.txt is used')
#                 return 0
#             if idiom_test(t,p) ==False:
#                 print('game over,you are out rules')
#             memory.add(p)
#             cycle_flag =0
#             while True:
#                 t = idiom_select(p)
#                 cycle_flag += 1
#                 if t not in memory:
#                     break
#                 if cycle_flag == 10:
#                     t = None
#                     break
#             if t == None:
#                 print('you win!!!')
#                 return 1
#             else:
#                 print(t)
#                 memory.add(t)
# idiom_start()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
