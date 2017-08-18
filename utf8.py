#-*-coding:utf8-*-
str='来自：Z9 Max'
res = str.encode('utf-8')
res=repr(res)


res = res[res.find("b") + 1:]

import re
strinfo = re.compile('\\\\x')
res = strinfo.sub('%',res)
strinfo = re.compile(' ')
res = strinfo.sub('%20',res)
res=eval(res)

print(res)

url0='https://pan.baidu.com/disk/home?errno=0&errmsg=Auth%20Login%20Sucess&&bduss=&ssnerror=0#list/vmode=grid&path=%2F'

url1=url0+res
print(url1)