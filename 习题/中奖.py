#while循环
import random
vol = random.randint(1,10)
guess = int(input('请输入1-10的数字，看看你有没有中奖'))
while True:
    if guess == vol:
        print('恭喜你猜对了')
        print('游戏结束')
        break
    elif guess > vol:
        guess = int(input('猜大了，没有中奖'))
        continue
    else:
        guess = int(input('猜小了，没有中奖'))
        continue

#for循环
# import random
# vol = random.randint(1,10)
# num = 3
# guess = int(input('请输入1-10的数字，看看你有没有中奖.总共有' + str(num) + '次机会'))
# for i in range(1, num + 1):
#     if guess == vol:
#         print('恭喜你猜对了')
#         print('游戏结束')
#         break
#     elif guess > vol:
#         guess = int(input('猜大了，没有中奖' + '你还有' + str(num - i) + '次计划'))
#     else:
#         guess = int(input('猜小了，没有中奖' + '你还有' + str(num - i) + '次计划'))
