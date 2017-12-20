#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author: 金鑫
# 2017/7/31
"""
30、购物车
功能要求：
要求用户输入总资产，例如：2000
显示商品列表，让用户根据序号选择商品，加入购物车
购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
goods = [{"name": "电脑", "price": 1999},
           {"name": "鼠标", "price": 10},
　　　　　　{"name": "游艇", "price": 20},
　　　　　　{"name": "美女", "price": 998},
]
"""
goods = [{"name": "电脑", "price": 1999},
         {"name": "鼠标", "price": 10},
         {"name": "游艇", "price": 5000000},
         {"name": "美女", "price": 998},
]


shopping_car = []
flag = True
while flag:
    asset_total = input('请输入你的总资产：')
    if asset_total.isdigit():
        asset_total = int(asset_total)
        print('*****请选择以下商品*****')
        for index,i in enumerate(goods,1):
            print('\t{0}\t{1}\t{2}'.format(index, i['name'], i['price']))
        print('************************')
        while True:
            goods_num = input('请选择您输入的商品序号(输入Q或者q为退出)：')
            if goods_num.isdigit():
                goods_num = int(goods_num)
                if goods_num > 0 and goods_num <= len(goods):
                    goods_price = goods[goods_num - 1]['price']
                    if asset_total >= goods_price:
                        asset_total = asset_total - goods_price
                        shopping_car.append(goods[goods_num - 1])
                        print('您已经成功购买%s,您的余额是%d' %(goods[goods_num - 1]['name'],asset_total))
                    else:print('您的余额不足')
                else:print('请输入正确的数字')
            elif goods_num.lower() == 'q':
                print('尊敬的VIP悦神，您已经购买了如下商品：')
                for i in shopping_car:
                    print(i)
                print('您的余额为： %s' %asset_total)
                flag = False
                break
            else:print("请输入数字")
    else:print('请输入正确的数字')