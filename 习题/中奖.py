import random
vol = random.randint(1,10)
guess = int(input('请输入1-10的数字，看看你有没有中奖'))
while guess != vol:
    if guess > vol:
        guess = int(input('猜大了，没有中奖'))
    else:
        guess = int(input('猜小了，没有中奖'))
else:
    print('恭喜你猜对了')
print('游戏结束')
