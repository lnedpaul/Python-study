# author: lnedpaul
#打印工作路径
import os
print(os.getcwd())

#抓取网站对象附给r
import requests
r = requests.get("http://www.youku.com")
print(r.url)
print(r.encoding)

#数据类型
import sys
a = 3
b = 4

c = 5.66
d = 8.0

e = complex(c,d)
f = complex(float(a), float(b))

print("a is type: ", type(a))
print("c is type: ", type(c))
print("e is type: ", type(e))

print(a + b)
print(d / c)
print(e + f)
print(sys.float_info)
