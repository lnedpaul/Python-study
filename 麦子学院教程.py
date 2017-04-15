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

#字符串
age = 3
name = 'Tom'
print("{0} was {1} years old".format(name,age))


#数据类型
nlist = [1,3,5,7,9]
slist = ['abc', 'bcd', 'cdf']
mixlist = ['python', 'java', 3, 8]
print("number list: " + str(nlist))
print("String list: " + str(slist))
print('mixed list: ' + str(mixlist))
second_num = nlist[1]
thrid_str = slist[2]
fourth_mixed = mixlist[3]
print('second number: {0} thrid string: {1} fourth mixed {2}'.format(second_num, thrid_str, fourth_mixed))
nlist[1] = 30
print('number list after: ' + str(nlist))
del nlist [1]
print('number list after del: ' + str(nlist))
a_tuple = (2,)
mixed_tuple = (1, 2, ['a', 'b'])
print('mixed tuple: ' + str(mixed_tuple))
mixed_tuple[2][0] = 'd'
mixed_tuple[2][1] = 'c'
print('mixed tuple after: ' + str(mixed_tuple))
citizen_number = {"Beijing":2171e4, "Shanghai":2415e4, "Chongqing":3017e4}
print (citizen_number["Shanghai"])
for ele in citizen_number:
    print(ele)
    print(citizen_number[ele])
for key, element in citizen_number.items():
    print(key, element)
