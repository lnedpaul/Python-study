#if 语句
number = 23
guess = int(input('Enter an integer : '))
if guess == number:
    # 新块从这里开始
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
    # 新块在这里结束
elif guess < number:
    # 另一代码块
    print('No, it is a little higher than that')
    # 你可以在此做任何你希望在该代码块内进行的事情
else:
    print('No, it is a little lower than that')
    # 你必须通过猜测一个大于（>）设置数的数字来到达这里。
print('Done')# 这最后一句语句将在 if 语句执行完毕后执行


#while 语句
number = 23
running = True
while running:
    guess = int(input('Enter an integer : '))
    if guess == number:
        print('Congratulations, you guessed it.')
        # 这将导致 while 循环中止
        running = False
    elif guess < number:
        print('No, it is a little higher than that.')
    else:
        print('No, it is a little lower than that.')
else:
    print('The while loop is over.')
    # 在这里你可以做你想做的任何事
print('Done')


#for 循环
for i in range(1, 5):
    print(i)
else:
    print('The for loop is over')


#break 语句
while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    print('Length of the string is', len(s))
print('Done')


#continue 语句
while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    if len(s) < 3:
        print('Too small')
        continue
    print('Input is of sufficient length')
    # 自此处起继续进行其它任何处理


#def函数
def say_hello():
    # 该块属于这一函数
    print('hello world')# 函数结束
say_hello()  # 调用函数
say_hello()  # 再次调用函数


#函数参数：“形参”（Parameters）“实参”（Arguments）
def print_max(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')


# 直接传递字面值
print_max(3, 4)

x = 5
y = 7

print_max(x, y)# 以参数的形式传递变量


#局部（Local）变量
x = 50
def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)
func(x)
print('x is still', x)


#global 语句
x = 50
def func():
    global x
    print('x is', x)
    x = 2
    print('Changed global x to', x)
func()
print('Value of x is', x)


#默认参数值
def say(message, times=1):
    print(message * times)
say('Hello')
say('World', 5)


#关键字参数
def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)
func(3, 7)
func(25, c=24)
func(c=50, a=100)


#可变参数
def total(a=5, *numbers, **phonebook):
    print('a', a)
    #遍历元组中的所有项目
    for single_item in numbers:
        print('single_item', single_item)
    #遍历字典中的所有项目
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)
print(total(10,1,2,3,Jack=1123,John=2231,Inge=1560))


#return 语句
def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y
print(maximum(2, 3))


#DocStrings
def print_max(x, y):
    '''Prints the maximum of two numbers.打印两个数值中的最大数。
    The two values must be integers.这两个数都应该是整数'''
    # 如果可能，将其转换至整数类型
    x = int(x)
    y = int(y)
    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')
print_max(3, 5)
print(print_max.__doc__)

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

#list列表
user_name = ['paul_82']
add_name = ['paul_0_82','paul82.zhu']
user_name.append('lnedpaul ')#追加单个对象
user_name.extend(add_name)#追加多个对象的列表
user_name.insert(0,'E',)#插入对象到指定位置
print(user_name)
user_name.remove('E')#移除对象
len(user_name)
print(user_name)
member = user_name[1:]
name = member.pop(1)
del member#删除整个列表
name
