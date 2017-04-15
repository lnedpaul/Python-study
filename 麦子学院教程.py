# author: lnedpaul
#打印工作路径
import os
print(os.getcwd())


#抓取网站对象附给r
import requests
r = requests.get("http://www.youku.com")
print(r.url)
print(r.encoding)
