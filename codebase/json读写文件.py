import json
#---------利用json写入文件--------
f = open('json_file','w')
json.dump({'k':(1,2,3)},f)
f.close()
#---------利用json读取文件--------
with open('json_file') as f:
    ret = json.load(f)
    print(ret,type(ret))