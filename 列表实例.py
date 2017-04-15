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
