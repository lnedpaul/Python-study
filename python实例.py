#Python字符串
str = 'Hello World!'

print (str) #输出完整字符串
print (str[0]) #输出字符串中的第一个字符
print (str[2:5]) #输出字符串中第三个至第五个之间的字符串
print (str[2:]) #输出从第三个字符开始的字符串
print (str * 2) #输出字符串两次
print (str + "TEST") #输出连接的字符串

#Python列表
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (list) #输出完整列表
print (list[0]) #输出列表的第一个元素
print (list[1:3]) #输出第二个至第三个的元素
print (list[2:]) #输出从第三个开始至列表末尾的所有元素
print (tinylist * 2) #输出列表两次
print (list + tinylist) #打印组合的列表

#Python元组
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')

print (tuple) #输出完整元组
print (tuple[0]) #输出元组的第一个元素
print (tuple[1:3]) #输出第二个至第三个的元素
print (tuple[2:]) #输出从第三个开始至列表末尾的所有元素
print (tinytuple * 2) #输出元组两次
print (tuple + tinytuple) # 打印组合的元组

#Python 字典
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print (dict['one']) #输出键为'one' 的值
print (dict[2]) #输出键为 2 的值
print (tinydict) #输出完整的字典
print (tinydict.keys()) #输出所有键
print (tinydict.values()) #输出所有值

#Python算术运算符
a = 21
b = 10
c = 0

c = a + b
print("1-c的值为：",c)

c = a - b
print("2-c的值为：",c)

c = a * b
print("3-c的值为：",c)

c = a / b
print("4-c的值为：",c)

c = a % b
print("5-c的值为：",c)

# 修改变量 a 、b 、c
a = 2
b = 3
c = a**b
print("6-c的值为：",c)

a = 10
b = 5
c = a//b
print("7-c的值为：",c)

#Python比较运算符
a = 21
b = 10
c = 0

if ( a == b ):
    print ("1-a 等于 b")
else:
    print ("1-a 不等于 b")

if ( a != b ):
    print ("2-a 不等于 b")
else:
    print ("2-a 等于 b")

#if ( a <> b ):
#    print ("3-a 不等于 b")
#else:
#    print ("3-a 等于 b")

if ( a < b ):
    print ("4-a 小于 b")
else:
    print ("4-a 大于等于 b")

if ( a > b ):
    print ("5-a 大于 b")
else:
    print ("5-a 小于等于 b")

# 修改变量 a 和 b 的值
a = 5;
b = 20;
if ( a <= b ):
    print ("6-a 小于等于 b")
else:
    print ("6-a 大于 b")

if ( b >= a ):
    print ("7-b 大于等于 a")
else:
    print ("7-b 小于 a")
