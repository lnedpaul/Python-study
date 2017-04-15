you_num = input("我买了几个蛋")
A = int(you_num)
my_num = input("你买了几个蛋")
B = int(my_num)
if A == B :
    print("我两买的一样多")
else:
    if A > B:
        print("你比我多买了", A - B ,"个蛋")
    else:
        A < B
        print("你比我少买了", B - A ,"个蛋")
