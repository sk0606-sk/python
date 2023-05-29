import random

count = 5
a = random.randint(1, 9)
while True:
    b = int(input('请猜一个1-9的数字 '))
    if b > a:
        print('很遗憾你猜大了')
        print(a)
        count -= 1
        print(f'还有{count}次')
        if count == 0:
            print('猜数失败')
            break
    elif b < a:
        print('很遗憾你猜小了')
        print(a)
        count -= 1
        print(f'还有{count}次')
        if count == 0:
            print('猜数失败')
            break
    elif b == a:
        print('恭喜你，猜数成功')
        print(a)
        break
