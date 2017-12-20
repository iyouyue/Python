# 查找列表li中的元素，移除每个元素的空格，并找出以’A’或者’a’开头，并以’c’结尾的所有元素，
# 并添加到一个新列表中,最后循环打印这个新列表。
# li = [‘taibai ’,’alexC’,’AbC ’,’egon’,’ Ritian’,’ Wusir’,’  aqc’]
li = ['taibai','alexC','AbC','egon','ritian','wusir','aqc']
new_li = []
for i in li:
    j = i.strip()
    if j.startswith('a') and j[-1] == 'c':
        new_li.append(j)
for k in new_li:
    print(k)