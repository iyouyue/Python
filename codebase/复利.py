roe = input('回报率：')
year = input('year:')

ori = 10000
count = 1
while count <= int(year):
	output = ori*(1+int(roe)*0.01)**count
	print('第'+str(count)+'年:'+str(int(output)))
	count += 1

# 存入 本金
# 一年后,本金×（1＋利率）
# 两年后,[本金（1＋利率）]×（1＋利率） 
# 第一年利息计入本金生息
# 三年后,[本金（1＋利率）（1＋利率）]×（1＋利率）
# ……
# n年后,本金（1＋利率）＾n