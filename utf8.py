#-*-coding:utf8-*-
str='来自：Z9 Max'
res = str.encode('utf-8')


print(res)
res=res.decode('utf-8')
print(type(res))
print(res)