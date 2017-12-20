f = open('goods_list.txt',encoding='utf-8')
goods_list = []
for list in f:
    goods_dic = {'name':None,'price':None}
    list = list.strip()
    print(list)
    goods = list.split()       #分割列表
    print(goods)
    goods_dic['name'] = goods[0]
    goods_dic['price'] = goods[-1]
    goods_list.append(goods_dic)
print(goods_list)
f.close()

# 电脑  1999
# 鼠标  10
# 游艇  20
# 美女  998